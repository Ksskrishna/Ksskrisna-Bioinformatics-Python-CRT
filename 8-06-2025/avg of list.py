'''
5. Calculate the Average of Numbers in a Given List
Write a program to calculate and return the average (mean) of a list of numbers (integers or floats). 
If the list is empty, handle the case with a suitable message.
'''
num = int(input("enter the range of list: "))
list1 = []
for i in range(num):
    temp = float(input("enter the elements: "))
    list1.append(temp)
if(num>0):
    avg = (sum(list1))/num
    print(f"average (mean) of list = {avg}")
else:
    print("give a valid list")