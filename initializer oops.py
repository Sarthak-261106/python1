#__init__() method

class Student:

    def __init__(self,name,roll):
        print('calling the initializer')
        self.name=name
        self.roll=roll

    def study(arg):
        return "the student studies for 3 hours a day"

s1=Student('john',1001)

print(s1.__dict__)