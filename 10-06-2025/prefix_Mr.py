"""
write a py prog to take name as input from user including prefix (Mr/Ms)
print the gender classification of the name on basis of prefix
"""

name = input("enter the name with Mr/Ms.")
if name.startswith('Mr.') == True:
    print("Male")
elif name.startswith('Ms.') == True:
    print("Female")

