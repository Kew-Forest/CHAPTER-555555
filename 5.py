def goubi(num, n):
    sb = num ** (1/n)
    if num >= 0:
        print ("The answer is", sb)
    else:
        print("Enter a positive number")
num = int(input("What is the Num "))
n = int(input("What is the N: "))
goubi(num, n)
