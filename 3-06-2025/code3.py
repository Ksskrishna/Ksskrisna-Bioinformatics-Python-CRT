#python program to read int value as input from user and check weather it is a 2 digit number or not a 2 digit number
num1 = int(input())
res = "2 digit number" if(num1<=99 and num1>=10) or (num1>=-99 and num1<=-10) else "not a 2 digit integer"
print(f"{num1} is a {res}")