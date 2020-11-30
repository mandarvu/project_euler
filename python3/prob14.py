''' BRUTE FORCE PROGRAM '''

"""
def collatz_chain(n):
    cnt = 0
    while (n != 1):
        if (n % 2 == 0):
            n /= 2
        else:
            n = (3 * n) + 1
        cnt += 1
    return (cnt+1)

lst = []
for i in range(1, 1_000_000):
    # lst.append(collatz_chain(i))
    if (collatz_chain(i) == 525):
        print(i)
"""

''' IMPROVED PROGRAM '''

def collatz_chain(n):
    if n % 2 == 0:
        