from numpy import floor

def is_perf_sq(n):
    '''
    Function returns True if input integer is a perfect square; else returns False
    '''
    if (int(n**.5) == (n**.5)):
        return True
    else:
        return False

for i in range(1,1000):
    for j in range(1, 1000):
        if is_perf_sq(i**2 + j**2) and (i + j + int((i**2 + j**2)**0.5) == 1000):
            print(i * j * int((i**2 + j**2)**0.5))