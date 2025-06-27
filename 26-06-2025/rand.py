list_1=[]
list_2=[]
num=int(input("Enter number of elementsto be appended:"))
for i in range(num):
    temp=int(input("Enter number: "))
    list_1.append(temp)
print(list_1)
for i in range(num):
    if list_1[i] in list_2:
        pass
    else:
        list_2.append(list_1[i])
print(list_2.sort())
