age = int(input("Enter your age: "))
if(age < 18):
    wait_years = 18 - age
    print(f"Wait for {wait_years} years to apply for RTO licence")
elif(age >= 18 and age < 75):
    print("You are eligible for applying RTO licence.")
    print("Welcome to Pune RTO office")
else:
    print("You are over age bar")
    