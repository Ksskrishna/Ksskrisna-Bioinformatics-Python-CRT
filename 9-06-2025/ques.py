'''
write a py prog to  read a string as input from the user (including spaces) and print the string by trimming the spaces
'''
string = input("enter the string: ")
print(f"entered string is: {string}")
string_lst = string.split()
print(string_lst)
#trim it
joined = "".join(string_lst)
print(joined)