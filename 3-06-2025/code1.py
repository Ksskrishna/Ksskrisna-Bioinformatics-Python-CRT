#traditional code
'''num = int(input())
if(num>0):
    print(f"{num} is a Positive Integer")
elif(num<0):
    print(f"{num} is a Negative Integer")
else:
    print("Zero")
'''
#using less number of lines (uses turnary operator)
num = int(input())
res = "+ve number" if(num>0) else "-ve number"
print(f"{num} is {res}")