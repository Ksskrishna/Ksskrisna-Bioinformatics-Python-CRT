#write a python prog to sort a list of numbers wihtout using sort method
num = int(input())
list1=[]
temp=[]
for i in range(num):
    temp=int(input())
    list1.append(temp)
for i in range(len(list1)):
    for j in range(0, len(list1) - i - 1):
        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

print(list1)