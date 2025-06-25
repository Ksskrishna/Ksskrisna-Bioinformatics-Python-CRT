'''
comprehension:
    comprehension contains very compact code usually a single statment that perform a task
    list comprahenshion
    set comprahension
    dictionary comprahension
'''
'''
list comprahension
    represents creation of new list from an iterable object that ssatisfy the given condition
    syntax: 
        new_list = [expression for item in iterable_object if_statment]
        there can be zero or more if statments
        there can be one or multiple for loops
    ex:-
        lst1 = [i+1 for i in range(20)]
        lst2 = [i for i in range(20) if i%2==0]
        lst3 = [i for i in range(11) if i%2==0 if i%3==0]

'''
num = []
for i in range(11):
    num.append(i)
print(num)
#incrementing same using lit comprahension
#new_list = [expression for item in iterable_object if_statment]
new = [i for i in range(1,11)]
print(new)
'''
write a python prog to print even numbers from 1 to 1 using list comprahensio
'''
new1 = [i for i in range(1,11) if i%2==0]
print(new1)
