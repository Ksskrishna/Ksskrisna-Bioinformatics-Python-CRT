'''
Given a list of integers, write a program to find and return the second largest unique number in the list. 
If no such number exists (due to insufficient unique values), handle it appropriately
'''
num = [10, 20, 8, 35, 40, 50]
unique_num = list(set(num))
unique_num.sort(reverse=True)
print(unique_num)
if len(unique_num) > 1:
    print(f"Second largest unique number: {unique_num[1]}")
else:
    print("No second largest unique number exists.")