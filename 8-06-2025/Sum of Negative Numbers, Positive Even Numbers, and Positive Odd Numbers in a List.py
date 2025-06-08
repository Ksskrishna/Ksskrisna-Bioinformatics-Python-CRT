'''
6. Print Sum of Negative Numbers, Positive Even Numbers, and Positive Odd Numbers in a List
Write a program that takes a list of integers and calculates:

* The sum of all negative numbers
* The sum of all positive even numbers
* The sum of all positive odd numbers
  Display each sum clearly.
'''

num = int(input("enter the range of list: "))
even_sum = 0
even_lst = []
odd_lst = []
list1 = []
for i in range(num):
    temp = int(input("enter the elements: "))
    list1.append(temp)
    
    if(list1[i]%2==0):
        even_lst.append(list1[i])
    else:
        odd_lst.append(list1[i])

print(f"even list = {even_lst}")
print(f"odd list = {odd_lst}")

print(f"sum of even list = {sum(even_lst)}")
print(f"sum of odd list = {sum(odd_lst)}")