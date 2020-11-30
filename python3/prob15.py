# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:32:04 2020

@author: mandarupasani

projecteuler.net
Problem no.19: Lattice Paths
"""

def no_of_paths(n):
    paths = 0
    temp = 0
    if (n == 2):
        return (6)
    cnt = 4
    while (n > 2):
        temp += no_of_paths(n-1) + cnt
        cnt += 1
        n -= 1
    paths = 2 * temp
    
    return (paths)