def sortedList(t1, t2, t3):
    l2 = [] #Detta kommer vara listan som fylls med tal
    if t1<=t2 and t1<=t3: #Om första talet är minst
        l2.append(t1)
        if t2<= t3:
            l2.append(t2)
            l2.append(t3)
        else:
            l2.append(t3)
            l2.a
    elif t2<=t1 and t2<=t3:
        l2.append(t2)
        if t1<= t3:
            l2.append(t1)
            l2.append(t3)
        else:
            l2.append(t3)
            l2.append(t1)
    else:
        l2.append(t3)
        if t1<= t2:
            l2.append(t1)
            l2.append(t2)
        else:
            l2.append(t2)
            l2.append(t1)
    return l2


tal1 = float(input("Skriv första tal: "))
tal2 = float(input("Skriv andra tal: "))
tal3 = float(input("Skriv tredje tal: "))

list1 = [tal1, tal2, tal3]
print(list1)

list2 = sortedList(tal1, tal2, tal3)
list3 = []
for element in list1:
    list3.append(element)
for element in list2:
    list3.append(element)

for element in list3:
    print(str(element) + "+")

