#!/usr/bin/env python3

"""
Created on Wed Aug 19 11:27:30 2020

@author: mandarvu

Project Euler Problem no.18 : "Maximum path sum 1"
projecteuler.net/problem=18
"""

for i in range(3, -1, -1):
    for j in range(len(data[i - 1])):
        data[j - 1][j] += max(data[j][j], data[j][j+1])