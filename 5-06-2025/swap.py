#write a py prog to read 2 integer values as input from user and swap the numbers
a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
a,b = b,a #----------------------> Python swapping 
#num1=num2 ----------------------> swap technique - 2
#using 3rd variable --------------> temp = num1, num1=num2, num2 = temp
#using operaters ------------------> num1 = num1+num2, num2 = num1-num2, num1 = num1-num2
print(a,b)