#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:28:44 2023

@author: tveloz
"""

# main.py (or another script)

from pyCOT_constructor import *
import networkx as nx
# Create an instance of the HelloWorld class
SpBt=bt([True,True,True,True])  # Default: [a, b, c, d]
SpId= np.array([1, 2, 3, 4])  # Default: [1, 0, 0, 0]
SpStr= ['a', 'b', 'c', 'd']  # Default: ['a', 'b', 'c', 'd']
RnStr= ['r1', 'r2']  # Updated: ['r1', 'r2']
RnVecId= np.array([1, 2])  # Updated: ['r1', 'r2']
RnBtS= bt([True, False])  # Default: [r1, r2]
RnBtP= bt([False, True])  # Default: [r1, r2]
RnVecS = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])  # Updated for reactions
RnVecP= np.array([[0, 2, 0, 0], [0, 1, 1, 0]])  # Updated for reactions

testRN=pyCOT(SpBt,SpId,SpStr,RnStr,RnVecId,RnBtS,RnBtP,RnVecS,RnVecP)

print(SpBt)
print(SpId)
print(SpStr)
print(RnBtS)
print(RnBtP)
print(RnVecId)
print(RnVecS)
print(RnVecP)






