file = open("testDoc.txt", "r+")
print(file.read())

file.write("\nadding a new line...")

file.close()