'''
read month nuber as input from user and print the respective number of days present in that particular days 
'''
num = int(input("enter a month number: "))
if num in [4,6,9,11]:
    print("30 days")
elif num in [1,3,5,7,8,10,12]:
    print("31 Days")
elif num == 2:
    print("28 or 29 days")
else:
    print("Invalid Month number")