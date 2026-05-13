name = input("What is your name? ")
salary = int(input("What is your salary? "))

HRA = (salary * 10) / 100
DA = (salary * 20) / 100
PF = (salary * 12) / 100
Total = salary + HRA + DA + PF

print("=" * 30)
print("Salary Slip of ", name)
print("=" * 30)
print("HRA is : ", HRA)
print("=" * 30)
print("DA is : ", DA)
print("=" * 30)
print("PF is : ", PF)
print("=" * 30)
print("Total Salary is : ", Total)
print("=" * 30)