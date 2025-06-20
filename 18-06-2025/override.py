'''
overriding
proving the specific method implementation for inherited methods from super class to subclass
'''
'''
overloading
occurs in same class
parameters are different
'''
class Graduation():
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratualtions you are a graduate now")
class CSE(Graduation):
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratukations you are a cs grad")
class Bioinformatics(Graduation):
    @staticmethod
    def Graduate():
        print("congo bi grad")
class ECE(Graduation):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Graduate():
        print("Congo ECE grad")
Graduation.Graduate()
CSE.Graduate()
Bioinformatics.Graduate()
ECE.Graduate()