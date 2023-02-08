kuvertArea = 2*0.229*0.324
affischArea = 2*0.297*0.420
infoBladArea= 0.210*0.297

ytviktKuvert = float(input("Kuvert ytvikt: "))
ytviktAffisch = float(input("Affisch ytvikt: "))
ytviktInfoBlad = float(input("Infobladets ytvikt: "))

totalVikt = kuvertArea*ytviktKuvert + affischArea*ytviktAffisch +\
            infoBladArea*ytviktInfoBlad
print(totalVikt)