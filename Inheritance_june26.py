#Single Inheritance
# class Parent:
#     def m1(self):
#         print(1)

# class child(Parent):
#     def m2(self):
#         print(2)

# p1 = Parent()
# p1.m1()
# #p1.m2()

# jay = child()
# jay.m1()
# jay.m2()

#Multilevel inheritance

# class GrandParent():
#     def m1(self):
#         print("GrandParent")

# class Parent(GrandParent):
#     def m2(self):
#         print("Parent")

# class Child(Parent):
#     def m3(self):
#         print("Child")


# c1 = Child()
# c1.m1()
# c1.m2()
# c1.m3()
# print(Child, __doc__)
# print(Child.mro())

#Hierarchical Inheritance
# class Parent():
#     def m1(self):
#         print("Parent")

# class Child1(Parent):
#     def m2(self):
#         print("Child1")

# class Child2(Parent):
#     def m3(self):
#         print("Child2")

# class Child3(Parent):
#     def m4(self):
#         print("Child3")

# c1 = Child1()
# c1.m1()
# c1.m2()

# c2 = Child2()
# c2.m1()
# c2.m3()

# c3 = Child3()
# c3.m1()
# c3.m4()

#Multiple Inheritance
# class Parent1(object):
#     def m1(self):
#         print("Parent1")

# class Parent2:
#     def m2(self):
#         print("Parent 2")

# class Child(Parent1,Parent2):
#     def m3(self):
#         print("Child")

# c1 = Child()
# c1.m1()
# c1.m2()
# print(Child.mro())

#super keyword used
class Parent:
    def __init__(self,fn,srn):
        self.fname = fn
        self.lastname = srn

    def m1(self):
        print(111)

class Child(Parent):
    """
    This is crated by xyz for ..... purpose
    """
    def __init__(self, fn, srn):
        self.fname = fn
        self.lastname = srn
    def m2(self):
        super().m1()
        print(222)

jay = Child("Jay", "Patil")
jay.m2()
