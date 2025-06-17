'''
object is of represents 2 types
states of an object represents the properties or attribute
Behaviour of an object represents the funtionality or work done by object
'''
'''
technical representation of states -> Data members
technical representation of function -> functions/Methods
'''
class Employee():
    def __init__(self,empName,empID,designation,salary,deptname,country):
        print("object is created")
        self.EmpName = empName
        self.EmpID = empID
        self.Designation = designation
        self.Salary = salary
        self.Deptname = deptname
        self.Country = country
def Display_Details(self):
    print("****************************************")
    print(f"Employee Name: {self.EmpName}")
    print(f"Employee ID: {self.EmpID}")
    print(f"Employee Designatio: {self.Designation}")
    print(f"Employee Salary: {self.Salary}")
    print(f"Employee DeptName: {self.Deptname}")
    print(f"Employee Country: {self.Country}")
    print("****************************************")
E1 = Employee("Scott","EMP101","Data Scientist","100000","R&D","USA")
E2 = Employee("Rajesh","EMP102","Developer","50000","Development","India")
Display_Details(E2)
Display_Details(E1)
