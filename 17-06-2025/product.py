'''
write a python program to create a product class declare the states of the class as productname, productId, price, gst, Manifacture_data, expired date
initialize using parameterized constructer
access the elements of individual objects using instance method
and delcare mutater methods as set, product name, set product price.............. and change the values of their properties using mutator methods and print it
'''
class Product():
    def __init__(self,p_name,p_ID,p_price,p_gst,pm_date,pe_date):
        print("object is created")
        self.P_name = p_name
        self.P_ID = p_ID
        self.P_price = p_price
        self.P_gst = p_gst
        self.Pm_date = pm_date
        self.Pe_date = pe_date
    def Get_details(self):
        print(f"product name: {self.P_name}")
        print(f"product ID: {self.P_ID}")
        print(f"product price: {self.P_price}")
        print(f"product gst: {self.P_gst}")
        print(f"product manifacture date: {self.Pm_date}")
        print(f"product expiry date: {self.Pe_date}")
    def Set_values(self):
        self.P_name = "Samsung phone"
        self.P_ID = "14058"
        self.P_price = "50000"
        self.P_gst = "25%"
        self.Pm_date = "18-05-2026"
        self.Pe_date = "25-10-2029"
              
M1 = Product("MI phone","14036","20,000","20 %","20-11-2026","18-05-2030")
print("before changing")
M1.Get_details()
print("after changing")
M1.Set_values()
M1.Get_details()

