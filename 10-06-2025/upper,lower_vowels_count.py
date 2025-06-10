'''
write a py prog to read a string as input from the user and print the count of 
1. upper case vowels
2. lower case voewls
3. upper case Consonants
4. Lower case Consonants
'''
string = input("enter the string: ")
u_vowel = 0
l_vowel = 0
l_consonants = 0
u_consonants = 0
for i in string:
    if i.isalpha() and i.isupper():
        if i in 'AEIOU':
            u_vowel += 1
        else:
            u_consonants += 1
    if i.isalpha() and i.islower():
        if i in 'aeiou':
            l_vowel += 1
        else:
            l_consonants += 1
print(f"Lower case Vowels count = {l_vowel}")
print(f"upper case Vowels count = {u_vowel}")
print(f"Lower case consonants count = {l_consonants}")
print(f"upper case consonants count = {u_consonants}")


#without using builtin functions

str=input("Enter the input : ")
Uppercase_Vowels=0
Lowercase_Vowels=0
Uppercase_Consonants=0
Lowercase_Consonants=0
for ch in str:
    if(ch>='A' and ch<='Z'):
        if ch in 'AEIOU':
            Uppercase_Vowels+=1
        else:
            Uppercase_Consonants+=1
    elif(ch>='a' and ch<='z'):
        if ch in 'aeiou':
            Lowercase_Vowels+=1
        else:
            Lowercase_Consonants+=1
print(f"Count of Upper case  Vowels : {Uppercase_Vowels}")
print(f"Count of Lower case Vowels : {Lowercase_Vowels}")
print(f"Count of Upper case Consonants : {Uppercase_Consonants}")
print(f"Count of Lower case Consonants : {Lowercase_Consonants}")

