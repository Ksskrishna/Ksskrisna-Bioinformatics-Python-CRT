#write a py prog to print the reversed multiplication tables of 1 to n
num = int(input())
for i in range(1,10):
    for j in range(10,1,-1):
        print(f"{i} * {j} = {i*j}")