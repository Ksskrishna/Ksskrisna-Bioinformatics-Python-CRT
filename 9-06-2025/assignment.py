'''
read as input from user
1. print the string as a list of individual charecters
2. find the length of the string
3. find the minimum element after converting string into list
4. find the number of spaces present in the string without using any built in functions or methods
'''
string = input("enter the string: ")
count = 0
for i in range(len(string)):
    print(f"individual charecter: {string[i]}")
print(f"length of string is : {len(string)}")
str_list = list(string)
print(f"the minimum element of the string is: {min(str_list)}")
for i in range(len(string)):
    if string[i]==' ':
        count = count+1
print(f"spaces in string are: {count}")