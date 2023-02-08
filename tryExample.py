"""name = input("name: ")
age = int(input("age: "))
try:
    print(name+age)
    print(1)
except:
    print(name + str(age))
    print(2)
    """

for i in range(-10, 5):
    try:
        print(1/i)
    except:
        print(i/(i+1))