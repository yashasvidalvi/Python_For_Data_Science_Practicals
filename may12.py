age = int(input("Enter your age: "))
if(age > 0):
    if 18<= age < 75:
        print("You are eligible for applying RTO licence.")
    elif age < 18:
        print(f"Wait for {18 - age} years to apply for RTO licence.")
    else:
        print("Age Barred for applying RTO licence.")
else:
    print("Age can not be negative....Please enter valid age.")
    