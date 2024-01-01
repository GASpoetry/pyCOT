import numpy as np
from bitarray import bitarray as bt
from typing import List

#Created by Tomas Veloz - github.com/tveloz

class pyCOT:
    """
    Class representing pyCOT (Python Chemical Reaction and Species Object)

    Attributes:
    - SpBt: Bitarray identification for species
    - SpStr: List of strings (species names) identification
    - RnBt: Bitarray identification for reactions
    - RnVecS: Vector (numpy.array) identification support of reactions 
    - RnVecP: Vector (numpy.array) identification for products of reactions
    - RnStr: List of strings (reaction names) identification

    Methods:
    - __init__: Constructor method to initialize the class with the provided parameters.
    - get_id_from_bt: Function that returns a vector from bitarray representation.
    - set_bt_from_id: Function that returns bitarray from vector representation.
    """

    def __init__(self, SpStr: List[str], SpBt: bt, RnStr: List[str], RnBt: bt,
                 RnVecS: np.ndarray, RnVecP: np.ndarray):
        """
        Constructor for pyCOT class.

        Parameters:
        - SpBt: Bitarray identification for species
        - SpStr: List of strings (species names) identification
        - RnBt: Bitarray identification for reactions
        - RnVecS: Vector (numpy.array) identification support of reactions 
        - RnVecP: Vector (numpy.array) identification for products of reactions
        - RnStr: List of strings (reaction names) identification
        """
        # Species
        self.SpStr = SpStr
        self.SpBt = SpBt
        
        # Reactions
        self.RnStr = RnStr
        self.RnBt = RnBt
        self.RnVecS = RnVecS
        self.RnVecP = RnVecP
#############################################################################
#############Vector of position to bt transformations#######################
############################################################################
    def get_id_from_bt(self, bt: bt) -> List[int]:
        """Function that returns a vector from bitarray representation."""
        vec = [i for i in range(len(bt)) if bt[i] == 1]
        return vec

    def get_bt_from_id(self, vec: List[int],size) -> bt:
        """Function that returns bitarray from vector representation."""
        bt_array = bt(size)
        bt_array.setall(0)
        for i in vec:
            bt_array[i] = 1
        return bt_array
   
    
  #############################################################################
  #############bt From/To str representations###########################
  ############################################################################              
    def get_bt_from_species(self, specs):
        bitarray = bt(len(self.SpStr)) 
        bitarray.setall(0)
        for i in range(len(specs)):
            for j in range(len(bitarray)):         
                if specs[i]==self.SpStr[j]:              
                    bitarray[j]=True
        return bitarray
    
    def get_bt_from_reactions(self,reactions_set):
        bitarray = bt()
        
        for reactions in self.RnStr:
            if reactions in reactions_set:
                bitarray.append(True)
            else:
                bitarray.append(False)        
        return bitarray
    
    def get_species_from_bt(self, bitarray):
        species_list=self.SpStr
        if len(species_list) != len(bitarray):
            print("Error: bitarray input has different length than species set size, can't continue")
            return None
        else:
            selected_species = []
            for i in range(len(bitarray)):
                if bitarray[i]:
                    selected_species.append(species_list[i])
            return selected_species
    def get_reactions_from_bt(self, bitarray):
        selected_reactions = []
        if len(self.RnStr) != len(bitarray):
            print("Error: bitarray input has different length than reactions set size, can't continue")
            return None
        else:
            
            for i in range(len(bitarray)):
                if bitarray[i]:
                    selected_reactions.append(self.RnStr[i])
            return selected_reactions
    
    def get_bt_abstraction(self,vec,t):
        """Function that returns a the set of species with value larger than t in a vector"""
        bitarray=bt()
        for i in range(len(vec)):
            if vec[i]>t:
                bitarray.append(True)
            else:
                bitarray.append(False)
        return(bitarray)  
    
    def get_supp_bt_from_reaction(self,reaction_name,t=0):
        if reaction_name not in self.RnStr:
            print(f"Error: Reaction '{reaction_name}' not found in the reactions set.")
            return None
        else:
            reaction_index = self.RnStr.index(reaction_name)
            support_vec = self.RnVecS[reaction_index]
            support_bitarray = self.get_bt_abstraction(support_vec,t)
        return support_bitarray

    def get_prod_bt_from_reaction(self,reaction_name,t=0):
        if reaction_name not in self.RnStr:
            print(f"Error: Reaction '{reaction_name}' not found in the reactions set.")
            return None
        else:
            reaction_index = self.RnStr.index(reaction_name)
            product_vec = self.RnVecP[reaction_index]
            product_bitarray = self.get_bt_abstraction(product_vec, t)
        return product_bitarray

    
    #############################################################################
    ############# obtaining sets of species/reactions from one another########
    ############################################################################              
    
    
    def get_reactions_from_species(self, SpStr,t=0):
    # Get the bitarray for the given set of species
        species_bitarray = self.get_bt_from_species(SpStr)    
    # Initialize an empty bitarray for triggered reactions
        triggered_reactions_bitarray = bt(len(self.RnStr))
        triggered_reactions_bitarray.setall(0)
    # Iterate through reactants and check if the species can trigger the reaction
        for i in range(len(self.RnStr)):
            supp=self.RnVecS[i]
            supp_bt=self.get_bt_abstraction(supp,t)
            #checking if supp_bt is contained in species_bitarray
            if (supp_bt&species_bitarray)==supp_bt:
                triggered_reactions_bitarray[i]=True
            else:
                triggered_reactions_bitarray[i]=False     
        return self.get_reactions_from_bt(triggered_reactions_bitarray)   
     
    def get_supp_from_reactions(self,RnStr):
    
        reactions_bitarray=self.get_bt_from_reactions(RnStr)
        specs=bt(len(self.SpStr))
        specs.setall(0)
        for i in range(len(self.RnStr)):
            if reactions_bitarray[i]:
                supp=self.get_supp_bt_from_reaction(self.RnStr[i])
                specs=specs | supp
        return self.get_species_from_bt(specs)
    def get_prod_from_reactions(self,RnStr):
    
        reactions_bitarray=self.get_bt_from_reactions(RnStr)
        specs=bt(len(self.SpStr))
        specs.setall(0)
        for i in range(len(self.RnStr)):
            if reactions_bitarray[i]:
                prod=self.get_prod_bt_from_reaction(self.RnStr[i])
                specs=specs | prod
        return self.get_species_from_bt(specs)       
    def get_prod_from_species(self,SpStr):
        reactions=self.get_reactions_from_species(SpStr)
        prod=self.get_prod_from_reactions(reactions)
        return prod
    
    #############################################################################
    ############# relational properties of species/reactions#####################
    ############################################################################              
    
    def is_closed(self,SpStr):
        species_bitarray = self.get_bt_from_species(SpStr)
        reactions_list=self.get_reactions_from_species(SpStr)
        prod_of_reactions=self.get_prod_from_reactions(reactions_list)
        prod_bitarray=self.get_bt_from_species(prod_of_reactions)
        return (prod_bitarray | species_bitarray)==species_bitarray
        
        
       
    