# A program to solve Problem23 on projecteuler.net

# A Function to check whether a number is abundant or not
def abundancy_check(n):
    div = []
    for i in range(1,(n//2 + 1)):
        if ( n % i == 0):
            div.append(i)
            continue
    if ( sum(div) > n ):
        return (True)

for i in range(10, 101):
    if (abundancy_check(i)):
        print(i)
