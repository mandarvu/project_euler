#! /usr/bin/env python3

# This is solution to problem25 on projecteuler.net
# This script just outputs the final answer


enc = {} # A dictionary to contain the fibonacci numbers encountered

def fibo(n):
    nkey = str(n)
    if n == 1 or n == 2: # for n = 1, sequence values are defined to be 1
        enc.update({nkey:1})
        return 1
    else:
        if nkey in enc: # if the number is already encountered during recursion, use it
                        # and don't bother with counting it again
            return enc[nkey]
        else:           # if not, then calculate the number and store it for future use
            enc.update({nkey: fibo(n-1) + fibo(n-2)})
            return enc[nkey]

# By a hunch, I think that it would take at least 1000 terms before 
# the length of number becomes 1000. But, the function is fast enough 
# for you to start the count from 1, or 100, your choice.

cnt = 500

while (len(str(fibo(cnt))) < 1000 ): # run the loop until the length of fibonacci number reaches 1000
    cnt += 1

print (f"The required answer is: {cnt}")
