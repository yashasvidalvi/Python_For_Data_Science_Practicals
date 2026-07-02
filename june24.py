# class Student:
#     def __init__(self,r,n):
#         self.__roll = r
#         self.__name = n

#     def display(self):
#         print(self.__roll)
#         print(self.__name)

# s1 = Student(1,"Rahul")
# s1.__roll = 100
# print(s1.roll)
# print(s1.name)
# s1.display()


# class Student:
#     def __init__(self,r : int,n : str):
#         self.__roll = r
#         self.__name = n
    
#     def getRoll(self) -> int:
#         return self.__roll
#     def getName(self) -> str:
#         return self.__name
#     def setRoll(self,nr:int) -> None:
#         self.__roll = nr
#     def setName(self,nn: str) -> None:
#         self.__name = nn

# s1 = Student(1,"Rahul")
# roll = s1.getRoll()
# print(roll)
# s1.setRoll(100)
# roll = s1.getRoll()
# print(roll)

class Student:
    cname = "TKA"
    def __init__(cls,r):
        cls.roll = r

    @classmethod
    def display(cls):
        print(cls.cname)

    def display2(self):
        print(self.cname)

    @staticmethod
    def average(m1,m2,m3,m4,m5):
        s = m1+m2+m3+m4+m5
        avg = s/5
        print(avg)
s1 = Student(1)
print(s1.cname)
print(Student.cname)
Student.display()
s1.average(56,56,67,67,89)
