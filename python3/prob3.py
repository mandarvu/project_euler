from math import sqrt
try:
    n = int(input("Enter a Number: "))
except:
    print("I said, an integer for fuck's sake.")

def primes(n):
    last_factor = 1
    if (n%2 == 0):
        last_factor = 2
        n /= 2
        print(last_factor," ")
        while (n%2 == 0):
            n /= 2
            print(last_factor," ")
    else:
        last_factor = 1

    factor = 3

    max_fact = int(sqrt(n))

    while ((n > 1) and (factor <= max_fact)):
        if (n % factor == 0):
            print(factor," ")
            n /= factor
            last_factor = factor
            while (n % factor == 0):
                n /= factor
                print(factor," ")
            max_fact = int(sqrt(n))
        factor += 2

    if n == 1:
        print(last_factor," ")
    else:
        print(int(n)," ")
primes(n)
