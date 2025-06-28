'''
write a py prog to read the year as input from the user and check weather it is a leap year or not.
'''
year = int(input("enter the year: "))
if year%4==0 and year%100!=0 or year%400 == 0:
    print("Leap Year")
else:
    print("Not a leap year")