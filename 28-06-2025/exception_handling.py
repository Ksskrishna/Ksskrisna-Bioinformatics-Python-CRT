'''
exception: 
    an exception is a runtime error which can be handled by the programmer
    all exceptions are representwed as classes in python
types of exception:
    1.Builtin exception:
        exeptions which are already avaliable in python language.
        the base class for all built in exception is base exception class
    2.User defined exception:
        a programmer can create his own exceptations, called user-defined exceptation. 
base exception: exception ---------> standard error ------> arthematic error, assertionerror, syntax error, type error, EOFerror, runtime error, import error, name error
warning ------> depercationwarning
Exception handling:
    try -> the try block contains code which may cause exceptions
Syntax: 
    try:
        statments
    execpt - the except block is used to catch an exception that is aised in the try block
    there can be multiple except block for try block
syntax:-
    except ExceptionName:
Else -  This block will get executed irrespective of weather there is an exception or not 
Sytax:-
    finally:
        statments
we can write several except blocks for a single try block
we can write multiple except blocks to handle multiple exceptions
we can try block without except block without ay try block
we can not write exception any except blocks
finally block is always executed irrespective of weather there is an exception or not
else block is optional
finally block is optional
'''
num = 100
print("Program execution begins")
print(num)
try:
    print(num/0)
except ZeroDivisionError:
    print("Dividind with Zero gives an infitine value")
print("Program  Execution ends")