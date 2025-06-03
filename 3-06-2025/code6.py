#write a python prog to print multuplication table from 1 to n 
num1 = int(input())
for i in range(1,num1+1):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")