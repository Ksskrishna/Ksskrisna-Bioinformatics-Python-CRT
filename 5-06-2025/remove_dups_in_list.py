num = int(input("enter the range of the list: "))
list1 = []
unique_toys=[]
for i in range(num):
    temp = input("Enter the names of toys: ")
    list1.append(temp)
for i in list1:    
    if i not in unique_toys:
        unique_toys.append(i)
print(list1)
print(unique_toys)