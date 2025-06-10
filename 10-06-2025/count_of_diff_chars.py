'''
write a py prog to read a string as input from the user and
1. print number of upper case letter count
2. print count of lower case letters
3. print the count of numeric values
4. print the count of spl chars
'''

string = input("enter the string: ")
count_upper = 0
count_lower = 0
count_digit = 0
count_spl = 0
for i in range(len(string)):
    if string[i].isupper():
        count_upper +=1
    elif string[i].islower():
        count_lower += 1
    elif string[i].isdigit():
        count_digit += 1
    else:
        count_spl += 1
print(f"upper_case count : {count_upper}")
print(f"lower_case count : {count_lower}")
print(f"digit_count : {count_digit}")
print(f"spl_char_count : {count_spl}")

