#n to 1
n = int(input())
def natural_numbers(n):
    if n==0:
        return
    natural_numbers(n-1)
    print(n)
natural_numbers(n)