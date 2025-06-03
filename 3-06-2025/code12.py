#write a py prog to read an integer value and print number of even digits and odd digits in that number
num = int(input())
even_count = 0
odd_count = 0
rem = 0
while(num!=0):
    rem = num%10
    if(rem%2==0):
        even_count=even_count+1
    elif(rem%2!=0):
        odd_count = odd_count+1
    num = num//10
print(even_count)
print(odd_count)