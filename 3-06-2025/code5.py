#write a py program to read an integer value as input from the user and print the multiplication table of it
num1 = int(input())
for i in range(1,11):
    print(f"{num1} * {i} = {i*num1}")