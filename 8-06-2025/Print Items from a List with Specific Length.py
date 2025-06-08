'''
2. Print Items from a List with Specific Length
You are given a list of strings and an integer n. 
Write a program that prints all the strings from the list that have a length exactly equal to n.
'''

num2 = int(input("enter how many elements in list: "))
list1 = []
for i in range(num2):
    temp = int(input("enter elements in list: "))
    list1.append(temp)
num = int(input("enter list range: "))
for i in range(num):
    print(list1[i])