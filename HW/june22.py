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
        self.mobileNumber = mo


obj_p = Phone("yashasvidalvi3@gmail.com",[7620027743,5345454354,5634643646])
obj_t = Teacher("Siya",54000,obj_p)
obj_s = Student("Shruti",12,obj_p)
obj_c = College(obj_s,obj_t)
print(obj_t.name)