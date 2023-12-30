#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 15:31:23 2023

@author: tveloz
"""

from bitarray import bitarray
import numpy as np
from pyCOT_constructor import *
import re
from collections import OrderedDict
import numpy as np
def extract_species_and_reactions(file_path):
    species_set = OrderedDict()
    reactions_set = OrderedDict()

    with open(file_path, 'r') as file:
        reaction_lines = file.read().split(';')

    for line in reaction_lines:
        line = line.strip()
        if line and not line.startswith('#'):
            # Extract reaction name and equation
            parts = line.split(':')
            reaction_name = parts[0].strip()
            reaction_equation = parts[1].strip()

            # Extract species from reactants and products
            species = re.findall(r'(\d*)?([a-zA-Z_]\w*)', reaction_equation)
            for coefficient, species_name in species:
                species_set[species_name] = None  # Using None as a placeholder

            # Add reaction name to the set
            #reac_name = re.findall(r'[Rr](_*\d+)+', reaction_name)  
            reactions_set[reaction_name] = None  # Using None as a placeholder

    unique_species = list(species_set.keys())
    reactions = list(reactions_set.keys())
    return unique_species, reactions

def build_stoichiometric_vectors(file_path, species_set):
    reactants_vectors = []
    products_vectors = []

    with open(file_path, 'r') as file:
        reaction_lines = file.read().split(';')

    for line in reaction_lines:
        line = line.strip()
        if line and not line.startswith('#'):
            # Extract reaction equation
            parts = line.split(':')
            reaction_equation = parts[1].strip()
            reactants, products = reaction_equation.split('=>')
            reactants = reactants.strip()
            products = products.strip()

            # Initialize vectors for reactants and products
            reactants_vector = np.zeros(len(species_set), dtype=int)
            products_vector = np.zeros(len(species_set), dtype=int)

            # Extract species and coefficients from reactants and products
            species_and_coefficients_reactants = re.findall(r'(\d*)?([a-zA-Z_]\w*)', reactants)
            species_and_coefficients_products = re.findall(r'(\d*)?([a-zA-Z_]\w*)', products)
            
            for coefficient, species_name in species_and_coefficients_reactants:
                species_index = species_set.index(species_name)
                stoichiometric_coefficient = int(coefficient) if coefficient else 1
                reactants_vector[species_index] = stoichiometric_coefficient
            for coefficient, species_name in species_and_coefficients_products:
                species_index = species_set.index(species_name)
                stoichiometric_coefficient = int(coefficient) if coefficient else 1
                products_vector[species_index] = stoichiometric_coefficient    

            reactants_vectors.append(reactants_vector)
            products_vectors.append(products_vector)

    return reactants_vectors, products_vectors
def load_pyCOT_from_file(file_path):
    species_set, reactions_list = extract_species_and_reactions(file_path)
    
    SpStr = list(species_set)
    SpBt = bt(len(SpStr))
    SpBt.setall(True)
    RnStr = reactions_list
    RnBt = bt(len(RnStr))
    RnBt.setall(True)
    RnVecS, RnVecP = build_stoichiometric_vectors(file_path, species_set)
    
    return pyCOT(SpStr, SpBt, RnStr, RnBt, RnVecS, RnVecP)