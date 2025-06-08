'''
Write a program that takes a list containing various data types, 
including None values. Your task is to count how many None values are present in the list and return the count.
'''
num = int(input("enter number of elements in the list: "))
count = 0
list1 = []
for i in range(num):
    temp = (input("enter element: "))
    list1.append(temp)
for i in list1:
    if i=='':
        count = count+1
        print(f"number of empty elements in list = {count}")