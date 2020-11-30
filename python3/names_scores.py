#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 12:25:13 2020

@author: mandarvu
Project Euler Problem no.22 : "Names scores"
projecteuler.net/problem=22
"""
#%% Generating alphabet score dictionary
X = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_values = {}
cnt = 1

for alpha in X:
    alphabet_values.update({str(alpha):cnt})
    cnt += 1
    
#%% Fuction to obtain worth of a name
def name_worth(name):
    """
    A function to return score of the input name

    Parameters
    ----------
    name : STR
        A Name is given as string

    Returns
    -------
        Sum of the numbers associated with each digit in the name
        eg, A = 1, M = 13.
    
    Example
    -------
    >>> name_score("COLIN")
    >>> 53
    """
    if name.upper() != name:
        name = name.upper()
    
    score = 0
    
    for letter in name:
        score += alphabet_values[str(letter)]
        
    return score

#%% Function to return the name score according to the formula

#%% Importing the data from the file
import numpy as np
names = np.loadtxt('p022_names.txt', dtype=str, delimiter=',')
names.sort()

#%% Main
count = 0
tot_score = 0
for name in names:
    target = name.strip('"')
    tot_score += name_worth(target) * ( count + 1 )
    count += 1
    
print(tot_score)