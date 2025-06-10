'''
replace all vowels with zeros
'''

string = input("enter the string: ")
modified = ""
for i in string:
    if i in 'AEIOUaeiou':
        modified += '0'
    else:
        modified += i
print(modified)