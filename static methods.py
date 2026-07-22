
class Student:
    college_name='abc college'
    departments=['physic','commerce','chemistry','arts']

    def __init__(self,name,roll):
        print('calling the initializer')
        self.name=name
        self.roll=roll

    def study(self,n):
        print(f"the student studies for {n} hours a day in {self.college_name}")

    @staticmethod
    def greet():
        print(f"hello")

    @classmethod
    def get_department(cls):
        print(f'department in {cls.college_name} are:')
        for department in cls.departments:
            print(department)


s1=Student('john',100)
s1.greet()

