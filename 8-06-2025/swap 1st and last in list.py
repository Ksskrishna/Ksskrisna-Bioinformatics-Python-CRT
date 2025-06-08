'''
4. Swap the First and Last Value of the Given List
Write a program that swaps the first and last elements of a given list and returns the updated list. 
The list may contain elements of any data type.
'''

num = int(input("enter the range of list: "))
list1=[]
for i in range(num):
    temp = input("enter elements in the list: ")
    list1.append(temp)

if(num>=2):
    list1[0],list1[-1] = list1[-1],list1[0]
    print(list1)
else:
    print(list1)