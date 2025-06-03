#python program to read integer value as the input from the user and check weather it is digit or number
num = int(input())
res = "digit" if(num<=9 and num>=-9) else "number"
print(f"{num} is {res}")