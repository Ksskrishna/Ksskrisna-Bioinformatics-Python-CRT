
'''
write a py prog to read name, contact number, mail id and password and make sure that
contact num has only 10 dig
mail should hava valid str following name@org_name.com 
password should have atleast
3 upper case alpha
3 lower case alpha 
3 spl charecters
and 1 number 
password length should not be less than 10
'''
mail = input("enter the mail: ")
count = 0
for i in mail:
    if i in "@" and ".com":
        count += 1
if count == 1 :
    print("Email is correct")
else:
    print("mail should be added with proper format")
number = list(input("enter mobile number: "))
if len(number) > 10 or len(number)<10:
    print("mobile number should be not more or less than 10")
else:
    print("Mobile number added")

password = input("Enter the password: ")

count_upper = 0
count_spl = 0
special_chars = "!#$%&'()*+,-./:;<=>?@[\\]^_{|}~"

if len(password) < 10:
    print("Password should be more than 10 characters")
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