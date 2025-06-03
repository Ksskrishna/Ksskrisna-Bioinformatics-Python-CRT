#write a py prog to print the reversed multiplication tables from n to 1
num = int(input())
for i in range(num,0,-1):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")