class Student:
    college_name='abc college'
    departments=['physic','commerce','chemistry','arts']

    def __init__(self,name,roll):
        print('calling the initializer')
        self.name=name
        self.roll=roll

    def study(arg):
        return "the student studies for 3 hours a day"


s1=Student('john',100)

print(s1.name)
print(s1.roll)
print(s1.departments)