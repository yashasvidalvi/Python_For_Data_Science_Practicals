# print("Start of the program")
# try:
#     num1 = int(input("Enter the first number:"))
#     num2 = int(input("Enter the second number:"))
#     print(num1/num2)

# except (ValueError, TypeError) as e:
#     print("pls enter valid interger")
#     print("Error:",e)

# except ZeroDivisionError as e:
#     print("Divison by zero is not allowed")
#     print("Error:",e)

# else:
#     print("Divsion successful")
# finally:
#     print("This block will always execute")
# print("End of the program")


class HumPadhaiNahiKarteException(Exception):
    pass

marks = int(input("Hey student pls enter your marks: "))

try:
    if marks < 40:
        obj = HumPadhaiNahiKarteException("Nahi karte padhai, marks kam hai")
        raise obj
    else:
        print("You are a good student")
    
except HumPadhaiNahiKarteException as e:
    print("insuffiencient balance")