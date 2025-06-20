'''
Functions/methods: 
    method overloading: 
        within the same class having multiple methods with same name but different parameters is called method overloading

'''
class Mobile():
    def __init__(self):
        print("Object is created")
def Unlock_mobile():
    print("swipe to unlock your mobile")
Unlock_mobile()
def Unlock_mobile(Password):
    print("Enter password to unlock your mobile")
    print(Password)
Unlock_mobile("XYZ")
def Unlock_mobile(num,Pattern):
    print("Enter your pin to eunlock your mobile")
    print(num,Pattern)
Unlock_mobile(4,"AAA")
