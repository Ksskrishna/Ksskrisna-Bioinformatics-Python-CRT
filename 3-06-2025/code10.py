#write a py prog to read an integer value from the user and find number of digits present in that particular number
#it should work even if negative numbers given
num = int(input())
temp = num 
dig_count=0
while(num>0 or num<0):
    num = num//10
    dig_count+=1
print(f"{temp} has {dig_count} digits")