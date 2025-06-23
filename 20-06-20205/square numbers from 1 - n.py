def square(n):
    if n==0:
        return 
    print(n*n)
    square(n-1)
square(5)

def square(n):
    if n==0:
        return
    square(n-1)
    print(n*n)
square(5)