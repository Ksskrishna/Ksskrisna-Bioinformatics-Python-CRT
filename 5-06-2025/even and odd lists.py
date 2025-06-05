size = int(input("enter the size of list: "))
list1=[]
even_list = []
odd_list = []
for i in range(size):
    temp = int(input("enter the elements in list: "))
    list1.append(temp)
    if(list1[i]%2==0):
        even_list.append(list1[i])
    else:
        odd_list.append(list1[i])
print(even_list)
print(odd_list)