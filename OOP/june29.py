class Book:
    def __init__(self,t,p):
        self.title = t
        self.price = p
    
    def __add__(self, other):
            return self.price + other.price
    
b1 = Book("Core Python ", 250)
b2 = Book("Data Analytics", 450)

print(b1 + b2)      


#print(b1.__add__(b2))

# class Student:
#     def __init__(self, r,n,m):
#         self.roll = r
#         self.name = n
#         self.marks = m

#     def __init__(self,r):  #Constructor Overloading
#         self.roll = r

#     def __init__(self, r,n):
#         self.roll = r
#         self.name = n


#     def display(self):
#         print(self.roll)
#     def display(self,r):
#         print(self.roll,self.name)  # Method Overloading

# #s1 = Student(1)
# s2 = Student(1,"Jay")
# #s3 = Student(1,"Jay",88)
# print(Student)