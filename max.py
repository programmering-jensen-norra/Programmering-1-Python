num1 = int(input("Write a number"))
num2 = int(input("Write a second number"))
num3 = int(input("Write a third number"))

if num1>num2 and num1>num3:
    print("The biggest one is " + str(num1))
elif num2>num1 and num2>num3:
    print("The biggest one is " + str(num2))
else:
    print("The biggest one is " + str(num3))