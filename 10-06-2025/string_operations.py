'''
#write a py prog to read the string as input the user and 
1. reverse the string 
2. convert the string in to lower case
3. conver the string in to upper case
4. convert the char of string to lower case if it is in upper case
5. convert to upper case if it is in lower case
6. check if the string is starting with the letter "A"
7. print the count of the charecter a from the given string and replace all letter "p" to letter "J"
'''
string = input("enter the string: ")
print(string[::-1])
print(string.lower())
print(string.upper())
print(string.swapcase())
print(string.startswith())
print(string.count('p'))
print(string.replace('P','j'))