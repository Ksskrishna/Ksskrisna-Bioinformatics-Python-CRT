'''
COnstructor overloading:
within the same class havinf multiple constructors with same name but different signature (paarmeters) is called constructor overloading.
'''

'''
write a py prog to create an employrr class and declare the states and create 5 objects using different constuctors
'''

#failed

class Employee:
    def __init__(self, *args):
        if len(args) == 6:
            self.Name = args[0]
            self.Id = args[1]
            self.Job = args[2]
            self.Salary = args[3]
            self.Location = args[4]
            self.Dept = args[5]
            print("object is created")
            print("Hey..! I'm a 6 parameterized constructor")
        elif len(args) == 3:
            self.Name = args[0]
            self.Id = args[1]
            self.Job = args[2]
            self.Salary = None
            self.Location = None
            self.Dept = None
            print("object is created")
            print("Hey..! I'm a 3 parameterized constructor")
        elif len(args) == 2:
            self.Name = args[0]
            self.Id = args[1]
            self.Job = None
            self.Salary = None
            self.Location = None
            self.Dept = None
            print("object is created")
            print("Hey..! I'm a 2 parameterized constructor")
        else:
            print("Invalid number of arguments")

# Usage examples:
emp1 = Employee("krishna", "101", "data scientist", "200000", "Hyd", "biotech")
emp2 = Employee("krishna", "101", "data scientist")
emp3 = Employee("krishna", "101")