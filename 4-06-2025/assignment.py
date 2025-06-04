#write a python prog to reverse a list of numbers without using reverse method 
num = int(input())
list1=[]
temp=[]
for i in range(num):
    temp=int(input())
    list1.append(temp)
print(f"without reversing {list1}")
print(f"after reversing {list1[::-1]}")
