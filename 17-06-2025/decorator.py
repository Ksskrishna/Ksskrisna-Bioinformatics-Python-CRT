class Mobile:
    def __init__(self):
        print("Object id created")
    @classmethod
    def Display(Class):
        print("I'm a class method")
        print("I will work irrespenctive of object creation")
Mobile.Display()

#using static method
class Mobile:
    def __init__(self):
        print("Object id created")
    @staticmethod
    def Display(): #should not call class method
        print("I'm a class method")
        print("I will work irrespenctive of object creation")
Mobile.Display()

'''
class methods are the methods which act upon the class variables or statoc variable of the class
'''
'''
static methods are used when some processing is related to the class but does not need the class or its instances to perform any work.
we use static methods when we want to pass some values from outside and perform some action in the method
Decorator @staticmthod need to write above static method
'''