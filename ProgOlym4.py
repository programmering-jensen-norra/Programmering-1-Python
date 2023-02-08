N = int(input("Ange tavlans storlek: "))
table = []
for i in range(N):
    table.append("Olle")
print(table)
print("For now, table is only a row")

for j in range(N):
    nyrad = []
    for i in range(N):
        nyrad.append(".")
    table[j] = nyrad

table[2][1] = "M"
for row in table:
    print(row)

