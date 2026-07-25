#method overriding

class Employee:
    def working_hours(self):
        return 45

class Intern(Employee):
    def working_hours(self):
        return 30


i1=Intern()
print(i1.working_hours())


















