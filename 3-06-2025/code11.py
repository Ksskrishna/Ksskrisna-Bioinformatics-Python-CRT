#write a py prog to read an integer value from the user and find summation of digits
num = int(input())
sum = 0
while(num!=0):
    rem = num % 10
    sum = sum+rem
    num = num//10
print(sum)

