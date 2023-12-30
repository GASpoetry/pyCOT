#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 15:31:23 2023

@author: tveloz
"""
import re
import numpy as np
from bitarray import bitarray


def parse_chemical_reactions(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    species_set = set(re.findall(r'\b[a-zA-Z]\b', ''.join(lines)))
    species_mapping = {species: index for index, species in enumerate(sorted(species_set))}
    
    sp_bt = bitarray([False] * len(species_mapping))
    sp_vec = np.zeros(len(species_mapping), dtype=int)
    sp_str = list(species_mapping.keys())

    rn_bt_s = bitarray()
    rn_bt_p = bitarray()
    rn_vec_s_list = []
    rn_vec_p_list = []
    rn_str_list = []

    for index, line in enumerate(lines):
        reaction_str = line.strip()
        reactants, products = map(str.strip, reaction_str.split('->'))

        rn_bt_s.append(True)  # Assume all reactions require support for simplicity
        rn_bt_p.append(True)  # Assume all reactions produce support for simplicity

        rn_vec_s = np.zeros(len(species_mapping), dtype=int)
        rn_vec_p = np.zeros(len(species_mapping), dtype=int)

        for reactant in re.findall(r'\b[a-zA-Z]\b', reactants):
            if reactant in species_mapping:
                rn_vec_s[species_mapping[reactant]] += 1

        for product in re.findall(r'\b[a-zA-Z]\b', products):
            if product in species_mapping:
                rn_vec_p[species_mapping[product]] += 1

        rn_vec_s_list.append(rn_vec_s)
        rn_vec_p_list.append(rn_vec_p)
        rn_str_list.append(f'r_{index+1}')  # Label each reaction as r_i where i is the index

    return pyCOT(SpBt=sp_bt, SpVec=sp_vec, SpStr=sp_str, RnBtS=rn_bt_s, RnBtP=rn_bt_p,
                 RnVecS=np.array(rn_vec_s_list), RnVecP=np.array(rn_vec_p_list), RnStr=rn_str_list)

# Example usage:
reactions_file_path = 'reactions.txt'
reaction_network_instance = parse_chemical_reactions(reactions_file_path)

# Accessing attributes of the instance
print("Species Bitarray:", reaction_network_instance.SpBt)
print("Species Vector:", reaction_network_instance.SpVec)
print("Species Names:", reaction_network_instance.SpStr)
print("Reaction Bitarray (Require Support):", reaction_network_instance.RnBtS)
print("Reaction Bitarray (Produce Support):", reaction_network_instance.RnBtP)
print("Reaction Vector (Require Support):", reaction_network_instance.RnVecS)
print("Reaction Vector (Produce Support):", reaction_network_instance.RnVecP)
print("Reaction Names:", reaction_network_instance.RnStr)

