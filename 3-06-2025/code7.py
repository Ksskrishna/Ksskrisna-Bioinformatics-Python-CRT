#write a py prog to print the reversed multiplication table of n
num = int(input())
for i in range(10,1,-1):
    print(f"{num} * {i} = {i*num}")
