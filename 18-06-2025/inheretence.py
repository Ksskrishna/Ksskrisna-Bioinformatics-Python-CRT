class Grandfather:
    def _init_(self):
        pass
    @staticmethod
    def properties():
        print("100 acres of land")
class Father(Grandfather):
    def _init_(self):
        super()._init_()
    @staticmethod
    def properties():
        print("50 acres of land")
class Yourself(Father):
    def _init_(self):
        super()._init_()
    @staticmethod
    def properties():
        print("A BTech degree")
Grandfather.properties()
Father.properties()
Yourself.properties()