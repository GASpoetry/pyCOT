#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 18:55:14 2023

@author: tveloz
"""
import numpy as np
import pandas as pd
import re
from bs4 import BeautifulSoup as bs
import copy
from bitarray import bitarray as bt
from bitarray import frozenbitarray as fbt
from scipy.optimize import linprog
import random as rm
import matplotlib.pyplot as plt
from pyvis.network import Network
import networkx as nx
from itertools import combinations
from Displays import *
from pyCOT_relational_properties import *

# Function that returns bitarray from vector represntation    
def BttoVec(bt):
    vec=[]
    for i in range(len(bt)):
        if bt[i]==1:
            vec.append(i)
    
    return vec

# Function that returns bitarray from vector represntation    
def VectoBt(vec,size):
    btarray=bt(size)
    btarray.setall(0)
    for i in ind:
       btarray[i]=1

    return btarray
