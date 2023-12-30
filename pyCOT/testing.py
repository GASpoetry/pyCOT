#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:28:44 2023

@author: tveloz
"""

# main.py (or another script)

from pyCOT_constructor import *
import networkx as nx
from File_manipulation import *

# Create an instance of the HelloWorld class
SpStr= ['a', 'b', 'c', 'd']  # Default: ['a', 'b', 'c', 'd']
SpBt=bt([True,True,True,True])  # Default: [a, b, c, d]
RnStr= ['r1', 'r2']  # Updated: ['r1', 'r2']
RnBt= bt([True, True])  # Default: [r1, r2]
RnVecS = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])  # Updated for reactions
RnVecP= np.array([[0, 2, 0, 0], [0, 1, 1, 0]])  # Updated for reactions

testRN=pyCOT(SpStr,SpBt,RnStr,RnBt,RnVecS,RnVecP)
print("specs")
print(testRN.SpStr)
print("specsBt")
print(testRN.SpBt)
print("reacsBt")
print(testRN.RnBt)
print("Reac")
print(testRN.RnStr)
print("SuppVec")
print(testRN.RnVecS)
print("ProdVec")
print(testRN.RnVecP)
# Example usage:
file_path = '../networks/autopoietic_ext.txt'
testRN2 = load_pyCOT_from_file(file_path)
print("specs")
print(testRN2.SpStr)
print("specsBt")
print(testRN2.SpBt)
print("reacsBt")
print(testRN2.RnBt)
print("Reac")
print(testRN2.RnStr)
print("SuppVec")
print(testRN2.RnVecS)
print("ProdVec")
print(testRN2.RnVecP[1])
print("bt_from_species")
print(testRN2.get_bt_from_species(['l','s2']))
print("species_from_bt")
print(testRN2.get_species_from_bt(bt('0011')))

print("bt_from_reactions")
print(testRN2.get_bt_from_reactions(['R1','R8']))
print("reactions_from_bt")
print(testRN2.get_reactions_from_bt(bt('00110011')))
print("support_bt_from_reaction")
print(testRN2.get_supp_bt_from_reaction('R1'),1)
print("products_bt_from_reaction")
print(testRN2.get_prod_bt_from_reaction('R4'))
print("contains")
print(testRN2.contains(bt('111'),bt('100')))
print("reactions_from_species")
print(testRN2.get_reactions_from_species(['l']))