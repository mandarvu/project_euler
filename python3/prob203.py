# Project Euler Problem No. 203
# projecteuler.net 
# Squarefree Binomial coefficients
# Created on Tue Aug 11 20:17:39 2020


#%% A Binomial coefficinet function (n choose k) 
from math import factorial as fact

def Binomial(n, r):
    """
    A finction which returns the binomial coefficient "n choose r"
    
    Parameters
    ----------
    n : Int
        Total number of available options.
    r : Int
        Number of options to be chosen.

    Returns
    -------
    ans : Int
        ( n )
        ( r )
        
        ans = (n!)/((n-r)! * (r)!)
    """
    try:    
        if (r > n): raise     
        if (r > (n/2)): 
        # Using the fact that (n r) = (n n-r) where '()' denotes binomial coeff
            r = n - r
        ans = fact(n) / (fact(n-r)*fact(r))
        return int(ans)
    except:
        print("Domain Error")
        print("r must be less than or equal to n")
    return 
        

#%% A function to check whether a number is square free or not

def is_square_free(num):
    """
    A function to check whether a number is square free or not

    Parameters
    ----------
   num : INT
        An input integer.

    Returns
    -------
    bool
        True if 'num' is square free, false elsewise.
    """
    for i in range(2, int(num ** 0.5) + 1):
        if (num % (i**2) == 0):
            return False
    return True

#%% Main frame

list1 = set()

for i in range(51):
    for j in range((i // 2) + 1):
        target = Binomial(i, j) 
        if not (target in list1) and is_square_free(target):
            list1.add(target)
            
#%% Final result calculation
print(sum(jj for jj in list1))