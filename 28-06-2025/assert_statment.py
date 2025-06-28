'''
the assert statment is useful to ensure that a given condition is true
if it is not true, it raises assertion error
syntax: assert condition, error message
    if the condition is false then the exception by the name assertion error is raised along with the message
    if message is not given and the codition is false then also assertion- error is raised with no message
Raising exception   
    raise statment is used to raise the user defined exception.
    raise myException('message')
'''
#raising exception
a = 20
assert a<= 10, 'Invalid Number'
