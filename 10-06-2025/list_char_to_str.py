'''
write a python progam to read the list of charecters as input from the user and convert it into a word and print it
'''
num = int(input("enter num of chars: "))
string_lst = []
for i in range(num):
    temp =  input("enter the chars: ")
    string_lst.append(temp)
print(string_lst)
str = "".join(string_lst)
print(str)
print(type(str))