'''
write a python program to check weather the user given integer is a even or odd using functions
'''
def even_odd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
num = int(input("enter the number"))
even_odd(num)