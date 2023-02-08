import random

import numpy as np
print("programming")
for i in range(10):
    print(random.gauss(50, 100))

list1 = ["matte", "programmering", "svenska", "engelska", "teknik"]
print(random.sample(list1, k=2))


a = 5
b = 4
c = np.sqrt(a*a + b*b)
print(str(c))