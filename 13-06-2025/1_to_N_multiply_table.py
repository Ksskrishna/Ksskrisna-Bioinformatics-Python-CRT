def table(num):
    for i in range(10):
        for j in range(10):
            print(f"{i} * {j} = {j*i}")
num = int(input("enter the number: "))
table(num)