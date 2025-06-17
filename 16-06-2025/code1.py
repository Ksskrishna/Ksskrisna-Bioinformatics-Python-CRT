'''
variable shadowing:
variable :- which holds the data temporarily
dominance of local variable over global variable
only when local and global variable are with same name
'''

greet = "good morning"
def display():
    greet = "good afternoon"
    print(greet)
display()

