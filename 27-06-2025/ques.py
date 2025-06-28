'''
write a py prog to read the month number as input from the user and check weather it is a valid month number or not
'''
num = int(input("enter month number"))
if(num>=1 and num<=12):
    print("Valid month number")
else:
    print("In-valid month number")

