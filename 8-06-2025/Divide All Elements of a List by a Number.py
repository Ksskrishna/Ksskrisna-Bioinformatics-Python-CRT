'''
Write a program that accepts a list of numbers and a divisor. 
Divide each element of the list by the divisor and return a new list with the results. Ensure the divisor is not zero.
'''
divisor = int(input("enter the divisor: "))
num = int(input("enter the range of list: "))

divisor_lst = []
reminder_lst = []
list1=[]
for i in range(num):
    temp = int(input("enter elements in the list: "))
    list1.append(temp)
    if(divisor!=0):
        divisor_lst.append(list1[i]//divisor)
        reminder_lst.append(list1[i]%divisor)
print(f"the quotient list = {divisor_lst}")
print(f"the reminder list = {reminder_lst}")