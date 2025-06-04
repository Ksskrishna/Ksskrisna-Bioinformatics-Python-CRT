#write a py prog to read an integer value and find number of 0's present in user entered number
num = int(input())
count = 0
digits = 0
while(num!=0):
    digits = num%10
    if(digits == 0):
        count = count+1
    num = num//10
print(count)