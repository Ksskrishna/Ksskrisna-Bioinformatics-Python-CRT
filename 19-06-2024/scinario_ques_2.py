import numpy as np
orders = np.array([120,150,130,160,140,180,170])
sum = 0
for i in orders:
    sum = sum + i
print(sum)