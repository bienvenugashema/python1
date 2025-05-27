import math

class Circle:
    def __init__(self,radius: float):
        self.radius = radius

    def area(self):
        return f"Area is : {math.pi * math.pow(self.radius,2)}"
    
    def perimeter(self):
        return f"Perimeter is : {2*math.pi * self.radius}"

circle = Circle(45)

print(circle.area())
print(circle.perimeter())
