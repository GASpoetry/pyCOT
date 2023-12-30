import numpy as np
from bitarray import bitarray as bt
from typing import List

class pyCOT:
    """
    Class representing pyCOT (Python Chemical Reaction and Species Object)

    Attributes:
    - SpBt: Bitarray identification for species
    - SpVec: Vector (numpy.array) identification for species
    - SpStr: List of strings (species names) identification
    - RnBtS: Bitarray identification for support of reactions 
    - RnBtP: Bitarray identification for products of reactions 
    - RnVecS: Vector (numpy.array) identification support of reactions 
    - RnVecP: Vector (numpy.array) identification for products of reactions
    - RnStr: List of strings (reaction names) identification

    Methods:
    - __init__: Constructor method to initialize the class with the provided parameters.
    """

    def __init__(self, SpBt: bt, SpId: np.ndarray, SpStr: List[str],
                 RnBtS: bt, RnBtP: bt, RnVecId: np.ndarray, RnVecS: np.ndarray, RnVecP: np.ndarray, RnStr: List[str]):
        """
        Constructor for pyCOT class.

        Parameters:
        - SpBt: Bitarray identification for species
        - SpVec: Vector (numpy.array) identification for indexes of species
        - SpStr: List of strings (species names) identification
        - RnBtS: Bitarray identification for support of reactions 
        - RnBtP: Bitarray identification for products of reactions 
        - RnVecS: Vector (numpy.array) identification support of reactions 
        - RnVecP: Vector (numpy.array) identification for products of reactions
        - RnStr: List of strings (reaction names) identification
        - RnId: Vector (numpy.array) identification for indexes of reactions
        """
        #Species
        self.SpStr = SpStr
        self.SpId = SpId
        self.SpBt = SpBt
        #Reactions
        self.RnBtS = RnBtS
        self.RnBtP = RnBtP
        self.RnStr = RnStr
        self.RnVecId  = RnVecId 
        self.RnVecS = RnVecS
        self.RnVecP = RnVecP
     ########################################################   
    #### Methods to obtain one representation from another###
   ##########################################################
   
    # Function that returns vector from bitarray representation 
    def BttoVec(self,bt):
        vec=[]
        for i in range(len(bt)):
            if bt[i]==1:
                vec.append(i)      
        return vec

    # Function that returns bitarray from vector representation    
    def VectoBt(self,vec,size):
        btarray=bt(size)
        btarray.setall(0)
        for i in vec:
           btarray[i]=1
        return btarray
