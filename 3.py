num = int(input("What is the Number: "))
n = int(input("What is the power N: "))
sb = num ** n
if sb >= 0:
    print ("The answer is", sb)
else:
    print("Enter a positive number")