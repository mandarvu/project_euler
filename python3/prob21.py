# <codecell> Functions used (1)
def sum_of_prop_divisors(n):
    """
    A Function that returns the sum of divisors of a natural number.

    Parameters
    ----------
    n : Integer.
        Any positive integer.

    Returns
    -------
        Integer
        Sum of divisors of n.

    """
    lst = []
    for i in range(1,n):
        if (n % i == 0):
            lst.append(i)
    return sum(lst)
# <codecell> Finding amicable numbers without ignoring the condition 'a != b'
list1 = []
for i in range(1,10001):
    if (i == sum_of_prop_divisors(sum_of_prop_divisors(i))):
        list1.append(i)

# print(list1)


# <codecell> Final test
for j in range(len(list1)):
    if list1[j] == sum_of_prop_divisors(list1[j]):
        list1[j] = 0        

print(sum(list1))
