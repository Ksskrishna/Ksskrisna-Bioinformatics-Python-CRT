import numpy as np
goals = np.array([1,0,2,1,3])
sum = 0
avg = 0
for i in goals:
    sum = sum + i
avg = sum/len(goals)
print(avg)