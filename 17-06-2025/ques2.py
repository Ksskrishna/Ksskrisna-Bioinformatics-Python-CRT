'''
write a python program to create a square shape class & declare the properties as
Length, Breadth, Height
1)Calculate the area of square using Instance Methods
2)check whether the sides of squares are equal or not
3)calculate the perimeter of square
4)find the Diagonals of square using instance methods
5)Find the Side Length of square using Instance Methods
'''
class Square:
    def __init__(self,l,b,h):
        print("object is created")
        self.length = l
        self.breadth = b
        self.height = h

    def area(self):
        area = self.length*self.breadth
        print(f"area of square is: {area}")
    def sides_equal(self):
        if self.length == self.breadth == self.height:
            print("length and bredth are equal")
        else:
            print("length and bredth are not equal")

    def perimeter(self):
        perimeter = 4 * self.length
        print(f"perimeter of the square: {perimeter}")

    def diagonals(self):
        diagonals = self.length * (2 ** 0.5)
        print(f"diagonal of the square is: {diagonals}")

    def side_length (self):
        if self.length == self.breadth == self.height:
            print(f"side length of the square is: {self.length}")
        else:
            print("given parameters are not sqare parameters")

M1 = Square(20,20,20)
M1.area()
M1.sides_equal()
M1.perimeter()
M1.diagonals()
M1.side_length()