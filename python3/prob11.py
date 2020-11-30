#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 13:12:59 2020

@author: mandarupasani
"""

# import numpy as np
import pandas as pd

dataset = pd.read_csv('prob11_data.csv')
# print(dataset)
# type(dataset)
# x1 = dataset.iloc[0,:].values
# print (max(x1))
lst = []

for i in range(0, 20):
    x = dataset.iloc[i,:].values
    xx = max(x)
    lst.append(xx)    
    