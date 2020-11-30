def fibo(cnt):
    f1 = 1
    f2 = 1
    if cnt == 1 or cnt == 2:
        return 1
    else:    
        for i in range(3, cnt + 1):
            fn = f1 + f2
            f1 = f2
            f2 = fn
        return fn

summ = 0
for i in range(1, 35):
    if ( fibo(i) % 2 == 0):
        summ += fibo(i)

print(summ)
