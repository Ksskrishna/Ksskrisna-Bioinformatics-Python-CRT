'''
Mutator method ****************************************************
This method is used to access or read and modify data of variables
this method modify the data into variable
This is also called as setter method

Ex: 
def set_value(self):
def set_results(self):
def set_name(self):
def set_id(self):
'''
class Mobile():
    def __init__(self,P,C,B):
        print("object is created")
        self.price = P
        self.color = C
        self.Brand = B
        print("Object is Created")
    #using mutator
    def Set_color(self):
        self.color="Blue"
    def Get_Details(self):
        print(f"Color : {self.color}")
        print(f"Price : {self.price}")
        print(f"Brand : {self.Brand}")
M1 = Mobile("12,000","Black","Samsung")
M1.Get_Details()
print("after changing using setter")
M1.Set_color()
M1.Get_Details()

