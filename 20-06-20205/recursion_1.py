'''

write a python porgram to print the summation of list emlements using recursion

'''
n = int(input("enter the value off n:"))
i = 0
def natural_numbers(n,i):
    i = i+1
    if n==0:
        return
    natural_numbers(n-1,i)
    print(f"{i} method call")
natural_numbers(n,i)