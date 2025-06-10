'''
write the python program to read password as input from the user and check weather it is valid password or invalid password
conditions
password should have atleast
3 upper case alpha
3 lower case alpha 
3 spl charecters
and 1 number 
password length should not be less than 10
'''
password = input("Enter the password: ")

count_upper = 0
count_spl = 0
special_chars = "!#$%&'()*+,-./:;<=>?@[\\]^_{|}~"

if len(password) < 10:
    print("Password should be more than 8 characters")
else:
    for char in password:
        if char.isupper():
            count_upper += 1
        if char in special_chars:
            count_spl += 1
            
    if count_upper < 3:
        print("Password should contain at least 3 uppercase letters")
    elif count_spl < 3:
        print("Password should contain at least 3 special characters")
    else:
        print("Password created successfully")
