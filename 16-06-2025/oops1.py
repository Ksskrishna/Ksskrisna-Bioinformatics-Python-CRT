'''
Costructer builds
it automatically calls a new object in class
def __init__(self): - constructs
'''
class student:
    def __init__(self):
        print("Het..!, I'm a Constructer of Students")
        print("I will be automatically invoked when the object is created")
S1 = student()
S1 = student()
S1 = student()
S1 = student()
print(type(S1)) 

'''
python supports a special tyoe of method called constructor for initializing the instance variable of that class

A class constructor, if defined is called whenever a program creates an object of that class

A constructor is called only once at the tie of creating an instance

if 2 instances are created for a class, the constructor will be called for each instance

parameterixzed constructor: 

Parameterized constructor are once which have parameters (other than self) defined in the __init__ method's parameter list
this type of constructor can taje arguments from the user.

Non - parameterized constructor: 

it is also known as default constructor.
the __init__ methold includes a single parameter self
no other parameter are present in __init__'s parameter list
consequently, this constructor takes no arguments while creating a new object
Non-parameterized constructors assign default values to the attributes of class
'''
'''
The __init__() method
This is a magic method (dunder method) which can be used to initialize variables for classes (object)
every class has __init__ and this is executed when we initiate the class
you can also use the method to do anything yoiu want to do when the object is being created
we donot call the method expicitily
'''
'''
self keyword
self is a default variable that contains the memory address of the curret objects
This variable is used to refer all the instance variable and method
When we create object of a class, the object name contains the memory location of the object
this memory loaction is internally passed tpo self, as self knows the 
'''
