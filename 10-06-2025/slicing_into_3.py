'''
write a py prog to read a str as input from the user and split the string into 3 equal halves using slicing
'''
string = input("enter the sentence: ")
divide = len(string)//3
for i in range(0, len(string), divide):
    print(string[i:i+divide])
