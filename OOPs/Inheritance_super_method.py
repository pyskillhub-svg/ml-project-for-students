class Parent:
    def land(self):
        print("this land to my son")
class Child(Parent):
    def land(self):
        super().land()
        print("This land came from my father")

s1 = Child()
s1.land()