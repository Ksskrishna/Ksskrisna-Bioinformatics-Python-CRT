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
        print(self.EmpName)
        print(self.EmpID)
        print(self.Designation)
        print(self.Salary)
        print(self.Deptname)
        print(self.Country)
E1 = Employee("Scott","EMP101","Data Scientist","100000","R&D","USA")
E2 = Employee("Rajesh","EMP102","Developer","50000","Development","India")
E1.Display_Details()
