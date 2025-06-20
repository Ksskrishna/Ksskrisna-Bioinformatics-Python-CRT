import numpy as np
price = np.array([50,20,30])
quantity = np.array([2,5,3])
product = price * quantity
total = 0
for i in product:
    total += i
print(total)