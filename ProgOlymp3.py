vokaler = "aeiouy"
mening = input("skriv en mening på svenska: ")
arabiska = ""
kortaVokaler = []
n = len(mening)
for i in range(n-2):
    if mening[i] in vokaler:
        if (not(mening[i+1] in vokaler) and not(mening[i+2] in vokaler) ):
            kortaVokaler.append(i)
for i in range(n):
    if not(i in kortaVokaler):
        arabiska += mening[i]
print(arabiska[::-1])

