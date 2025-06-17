'''
write a py prog to check weather the number is positive or negative
'''
n = int(input("Enter a number: "))
val = lambda n: "Negative" if n < 0 else ("Zero" if(n==0) else "Positive")
print(f"{n} is {val(n)}")