from numpy import abs
def sum_of_nat_numbers(n):
    return int(n * (n + 1) / 2)

def sum_of_sq_of_nat_num(n):
    return int(n * (n + 1) * (2 * n + 1) / 6)

def diff(n):
    x = sum_of_sq_of_nat_num(n) - (sum_of_nat_numbers(n))**2
    return abs(x)
print(diff(100))
