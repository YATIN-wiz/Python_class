class Rectangle:
    def __init__(self, l,b):
        self.length = int(l)
        self.breadth = int(b)

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)

rec1 = Rectangle(input("Enter length:"),input("Enter breadth:"))
print("Area:", rec1.area())
print("Perimeter:", rec1.perimeter())

        

        
