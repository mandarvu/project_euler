def sum_of_nat_numbers(n):
    return int(n * (n + 1) / 2)
'''
for i in range(1,51):
    print(sum_of_nat_numbers(i)
'''

# for jj in range(1, 12):
jj = sum_of_nat_numbers(53)
lst = []
for i in range(1,jj+1):
    if (sum_of_nat_numbers(jj) % i == 0):
        lst.append(i)    
    
print(jj,len(lst))
