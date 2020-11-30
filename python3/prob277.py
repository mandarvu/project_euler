# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# string = ''
#%%
def collatz_seq(n, init):    
    if (init == 1):    
        global string, memoize 
        string = ''
        init = 0
        # memoize = dict()
    
    # str_lim = 10
    # if (len(string) == str_lim):
    #     return string
    
    if (n == 1):
        return string
    if (n % 3 == 0):
        string += 'D'
        
        collatz_seq(n // 3, init)
    elif (n % 3 == 1):
        string += 'U'
        collatz_seq(((4 * n) + 2) // 3, init)
    elif (n % 3 == 2):
        string += 'd'
        collatz_seq(((2 * n) - 1) // 3, init)

#%%        
count = 1000000000000001
while (True):
    target = 'UDDDUdddDDUDDddDdDddDDUDDdUUDd'
    obtained_string = collatz_seq(count, 1)
    if (obtained_string == target):
        print(count)
        break
    count += 3
