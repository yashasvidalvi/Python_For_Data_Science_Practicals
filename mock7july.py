class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Student(Person):
    def __init__(self, name,address,roll_no,marks):
        super().__init__(name, address)
        self.roll_no = roll_no
        self.marks = marks

class Scholarship(Student):
    def __init__(self, name,address,roll_no,marks):
        super().__init__(name, address, roll_no, marks)

    def check_eligibility(self):
        if self.marks >= 80:
            print(f"{self.name} is eligible for scholarship.")
        else:
            print(f"{self.name} is not eligible for scholarship.")

student1 = Scholarship("Siya", "Pune", 101, 21)
student1.check_eligibility()
