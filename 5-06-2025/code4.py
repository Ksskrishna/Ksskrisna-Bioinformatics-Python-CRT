#write a python to read the list elements as input from the user and check weather the list elements are multiples of 3 and 5 or not 
# and print the list of elements which are multiples of 3 and 5
#write a python prog to read the list elements as input from user and print a new list of numbers which are multiples of 5
num = int(input("enter the range of list:"))
list1=[]
list5=[]
for i in range (num):
    temp=int(input(f"Enter the integer value at {i} index : "))
    list1.append(temp)
    if(list1[i]%3==0 and list1[i]%5==0): # (i%5==0 and i%3==0)
        list5.append(list1[i])
print(f"original list: {list1}")
print(f"List with multiples of 3 and 5: {list5}")
