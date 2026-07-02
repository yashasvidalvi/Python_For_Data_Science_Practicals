# class Employee:
#     def __init__(self,nm,dep,add):
#         self.name = nm
#         self.department = dep
#         self.Address = add

# class Address:
#     def __init__(self,c,pin):
#         self.city = c
#         self.pincode = pin

# obj_a = Address("pune",411041)
# print(type(obj_a)) 
# print(obj_a.city)
# print(id(obj_a))
# obj_e = Employee("Sita","IT",obj_a)
# print(type(obj_e))
# print(obj_e.name)
# print(id(obj_e))
# print(id(obj_e.Address))

class College:
    def __init__(self,stu,tea):
        self.student = stu
        self.teacher = tea

class Student:
    def __init__(self,nm,roll,ph):
        self.name = nm
        self.roll = roll
        self.phone = ph

class Teacher:
    def __init__(self,nm,sal,ph):
        self.name = nm
        self.salary = sal
        self.phone = ph

class Phone:
    def __init__(self,em,mo):
        self.emailId = em
        self.number = mo

mob = [42343432434,3432432432,3243423,324432]
mob2 = [5436436,6456554,7567567,345235235]
ph1 = Phone("at@gmail.com",mob)
ph2 = Phone("xyz@gmail.com",mob2)

s1 = Student("Jay",1,ph1)
s2 = Student("Viru",2,ph1)
s3 = Student("Gabbar",3,ph1)
s4 = Student("Basanti",4,ph1)

t1 = Teacher("Rahul sir",55000,ph2)
t2 = Teacher("Amit Sir",550000,ph2)
t3 = Teacher("Kiran Sir",550000,ph2)
t4 = Teacher("Atul Sir",550000,ph2)

all_student_list = [s1,s2,s3,s4]
all_teacher_list = [t1,t2,t3,t4]

colg = College(all_student_list,all_teacher_list)

print(colg.student[0].name)

first_mob = colg.student[0].phone.number[0]
print(first_mob)