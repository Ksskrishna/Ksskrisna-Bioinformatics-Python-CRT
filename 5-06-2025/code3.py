#write a python prog to read the list elements as input from user and print a new list of numbers which are multiples of 5
num = int(input("enter the range of list:"))
list1=[]
temp = []
list5=[]
for i in range (num):
    temp = int(input())
    list1.append(temp)
    if(list1[i]%5==0):
        list5.append(list1[i])
print(f"original list: {list1}")
print(f"List with multiples of 5: {list5}")
