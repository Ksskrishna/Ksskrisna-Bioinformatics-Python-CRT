def table(num):
    for i in range(11):
        print(f"{num} * {i} = {num*i}")
num = int(input("enter the number: "))
table(num)