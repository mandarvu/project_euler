# Prject Euler problem no.69
# "projecteuler.net/problem=69"
# Created on Wed Aug 12 12:20:39 2020
# Totient maximum

#%% Prime Factor finder
def prime_factors(num):
    factors = list()
    if (num % 2 == 0):
        while( num % 2 == 0):
            factors.append(2)
            num //= 2
    i = 3
    while (num > 1):
        if (num % i == 0) and prime(i):
            while (num % i == 0):    
                factors.append(i)
                num //= i
        i += 2
    return factors

#%% Prime Checker
def prime(n):
    if (n % 2 == 0):
        return False
    else:
        for i in range(3, int(n**0.5)+1,2):
            if (n % i == 0):
                return False
    return True

#%% Euler phi-function (totient-function)
def euler_phi(num):
    temp = 1
    for i in set(prime_factors(num)):
        temp *= (1 - (1/i))
    return int( num * temp)

#%% Main frame
# answer is just the product of first smallest primes 2,3,5,7,11,13,17
# the answer is easily obtained by observation
# the functions defined above are quite useful though.