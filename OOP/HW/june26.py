#Multiple Inheritance
class p1:
    def m1(self):
        print("p1 is unique method called")
    def m5(self):
        print("m5 from p1")

class p2:
    def m2(self):
        print("p2 unique method called")
    def m5(self):
        print("m5 from p2")

class c(p1,p2):
    def m3(Self):
        print("child unique method called")

jay = c()
jay.m5()



#hybrid Inheritance
class GrandParent:
    def m5(self):
        print("m5 from gandparent")

class Parent1(GrandParent):
    def m5(self):
        print("m5 from Parent1")
class Parent2(GrandParent):
    def m5(self):
        print("m5 from Parent2")

class Child(Parent1, Parent2):
    def m2(self):
        print("m3 from child")

c1 = Child()
c1.m5()
