'''
write  a py prog to read mail id as input from the user and print user name and organisation name based on mail id
name@org_name.com
'''
mail = input("enter the mail_id: ")
mail_add = 0
for i in range(len(mail)):
    if(mail[i] == "@"):
        mail_add = i

print("user name is: ", end="")
for i in range(mail_add):
    print(mail[i], end="")

mail_1 = len(mail) 
for i in range(len(mail)):
    if(mail[i] == "."):
        mail_1 = i
        break 

print("\norganisation name is: ", end="")
for i in range(mail_add + 1, mail_1):
    print(mail[i], end="")

#logic -2
#write a py program tp read mail id as input from the user name and organisation name based on mail id (first : name@orgname  org.com )
mail_id=input("Enter the mail_id : ")
List=mail_id.split('@')
print(f"User Name : {List[0]}")
Org=List[1]
List=Org.split('.')
print(f" Org Name : {List[0]}")
"".removeprefix