class calculator:
    num = int(input("enter a number: "))

    def square(self):
        print("the square is: ", self.num * self.num)

    def cube(self):
        print("the cube is: ", self.num * self.num * self.num)   

    def squareroot(self):
        print("the square root is: ", self.num ** 0.5)

    @staticmethod
    def greet():
        print("hello welcome to the program")

a = calculator()
a.square()
a.squareroot()
a.cube()
a.greet()
