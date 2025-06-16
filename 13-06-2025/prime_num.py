'''
write a python program check weather the user given number is prime number or not using functions
(using return)
'''
def prime(num):
    count = 0
    for i in range(1,num+1):
        if (num % i==0):
            count += 1
    if count == 2:
        print("Prime")
    else:
        print("Not a prime number")

num = int(input("enter the number: "))
prime(num)
