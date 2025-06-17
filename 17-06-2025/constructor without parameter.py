'''
constructor without parameter
'''
#constructor
class Mobile:
    def __init__(self):
        print("Mobile Constructor Called")
realme = Mobile()

'''
constructor without parameter
'''
class Mobile:
    def __init__(self):
        self.model = "realMe x"
    def show_model(self):
        print(f"Model:",self.model)
realme = Mobile()
realme.show_model()

'''
types of methods:
1.instance method
    accessor method
    mutator method
2.class methods
3.static method
'''
