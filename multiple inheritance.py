class A:
    def state_1(self):
        print("state_1 present")
    def state_2(self):
        print("state_2 present")
class B:
    def state_3(self):
        print("state_3 present")
    def state_4(self):
        print("state_4 present")
class C(A,B):
    def state_5(self):
        print("state_5 present")

a=A()
a.state_1()

b=B()
b.state_3()

c=C()
c.state_1()