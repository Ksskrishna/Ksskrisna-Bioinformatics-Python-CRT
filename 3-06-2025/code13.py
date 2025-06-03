#write a py prog to read an integer value and find summation of even digits and odd digits present in that number
num = int(input())
even_sum=0
odd_sum=0
temp = num
rem = 0
while(num!=0):
    digits = num%10
    if(num%2==0):
        even_sum = even_sum+digits
    else:
        odd_sum = odd_sum+digits
    num = num//10
print(f"even sum of digits = {even_sum}")
print(f"odd sum of digits = {odd_sum}")