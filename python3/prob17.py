tens = ("","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety")
ones = ("","one", "two","three","four","five","six","seven","eight","nine")
specials = ("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen")

base = len("onethousand")

def num_in_words(n):
    num = str(n)
    if (n // 100 == 0):
        if (n >= 20) :    
            word = tens[int(num[0])] + ones[int(num[-1])]
            return word
        elif (n >= 10) and (n <= 19):
            word = specials[int(num[-1])]
            return word
        elif (n < 10):
            word = ones[n]
            return word
    elif (n % 100 != 0):
        word = ones[int(num[0])] + "hundredand" + num_in_words(n % 100)
        return word
    else:
        word = ones[int(num[0])] + "hundred"
        return word

summ = 0
for i in range(1,1000):
    summ += len(num_in_words(i))

'''x = int(input("Enter number: "))
print(num_in_words(x))'''
