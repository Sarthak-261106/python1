# class welcome():
#     @classmethod
#     def welcome(cls):
#         print(cls)
#         print('hello')
#
# w1=welcome()
# w1.welcome()

class Student:
    college_name='abc college'
    departments=['physic','commerce','chemistry','arts']

    def __init__(self,name,roll):
        print('calling the initializer')
        self.name=name
        self.roll=roll

    def study(self,n):
        print(f"the student studies for {n} hours a day")

    @classmethod
    def greet(cls):
        print("hello")


s1=Student('john',100)
s1.study(4)
s1.greet()
