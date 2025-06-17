'''
write a python program to create a mobile class and declare the states of mobile as color, price, brand, series, version, features, storaage, battery_capacity, ram, processoor
create 10 objects and initalize using constructor print the details of the indivual objects using function 
'''
class Mobile():
    def __init__(self, color, price, brand, series, version, features, storage, battery_capacity, ram, processor):
        print("Objects are created")
        self.Color = color
        self.Price = price
        self.Brand = brand
        self.Series = series
        self.Version = version
        self.Features = features
        self.Storage = storage
        self.Battery_capacity = battery_capacity
        self.Ram = ram
        self.Processor = processor
def Mobile_details(self):
    print(f"Mobile color: {self.Color}")
    print(f"Mobile price: {self.Price}")
    print(f"Mobile Brand: {self.Brand}")
    print(f"Mobile Series: {self.Series}")
    print(f"Mobile Version: {self.Version}")
    print(f"Mobile Features: {self.Features}")
    print(f"Mobile Storage: {self.Storage}")
    print(f"Mobile Battery Capacity: {self.Battery_capacity}")
    print(f"Mobile Ram: {self.Ram}")
    print(f"Mobile Processor: {self.Processor}")
    print("************************************")
M1 = Mobile("Olive Green","30,000","Samsung","S","23","Compact phone","256gb","3900mah","8gb","Snapdragon")
M2 = Mobile("Black","25,000","MI","X","0010","Good screen","128gb","6000mah","6gb","Snapdragon")
M3 = Mobile("Black","25,000","MI","X","0010","Good screen","128gb","6000mah","6gb","Snapdragon")
M4 = Mobile("Black","25,000","MI","X","0010","Good screen","128gb","6000mah","6gb","Snapdragon")
M5 = Mobile("Black","25,000","MI","X","0010","Good screen","128gb","6000mah","6gb","Snapdragon")
M6 = Mobile("Black","25,000","MI","X","0010","Good screen","128gb","6000mah","6gb","Snapdragon")
M7 = Mobile("Black","25,000","MI","X","0010","Good screen","128gb","6000mah","6gb","Snapdragon")
M8 = Mobile("Black","25,000","MI","X","0010","Good screen","128gb","6000mah","6gb","Snapdragon")
M9 = Mobile("Black","25,000","MI","X","0010","Good screen","128gb","6000mah","6gb","Snapdragon")
M10 = Mobile("Black","25,000","MI","X","0010","Good screen","128gb","6000mah","6gb","Snapdragon")
Mobile_details(M1)
Mobile_details(M2)
Mobile_details(M3)
Mobile_details(M4)
Mobile_details(M5)
Mobile_details(M6)
Mobile_details(M7)
Mobile_details(M8)
Mobile_details(M9)
Mobile_details(M10)

