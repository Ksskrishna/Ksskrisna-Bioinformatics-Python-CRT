'''
write a py prog to create a rectangle class and initialize the variable length and bredth using constructor 
and access the values using mutater methods 
'''
class Rectangle():
    def __init__(self, l, b):
        print("object is created")
        
        self.length = l
        
        self.bredth = b
    def Set_details(self):
        print(f"length of the rectagle is : {self.length}")
        print(f"bredth of the rectangle is : {self.bredth}")

l = input("enter length of rectangle: ")
b = input("enter the breadth of rectangle: ")

M1 = Rectangle(l,b)
M1.Set_details()