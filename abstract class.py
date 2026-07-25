from my_abstract_class import Shape



class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width


class Square():
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side*self.side

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.12*self.radius**2

s1=Square(5)
print(s1.area())

r1=Rectangle(3,4)
print(r1.area())

c1=Circle(5)
print(c1.area())