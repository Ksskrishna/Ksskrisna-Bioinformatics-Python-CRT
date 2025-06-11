'''
A Dictonary represents a group of elements in the form of key value pairs
Dictonary in python is an unordered collection.
ddictonary in python is an unordered collection
Dictonaries are mutable so we can modify it's item, without changing their idemntity.
represented by curly braces {}
'''
exu = {101:'Python',102:'Java',103:'javascript',104:'SQL',105:'C'}
#accessing by dict[key]
print(type(exu))
print(exu[101])

'''
Rules:
While writing key we must follow following rules
1. key should be unique
2. if we mention same key again the old key will be overwritten
3. key should be immutable type ex: integer, string, tuple
4. we cannot use the same...........
'''
stu = {200:'Rahul',201:'Raj',202:'Suman'}
fees = {'Rahul':2000,'Raj':3000,'Suman':4000}
print(fees['Rahul'])
print(fees['Raj'])
print(fees['Suman'])
print(stu[200],stu[201])

#updation or modifiation of an element
stu = {200:'Rahul',201:'Raj',202:'Suman'}
stu[200] = 'Rakul'
print(stu)
#addition of an element
stu[400] = "Suman"
print(stu)
#deletion
del stu[200]
print(stu)