# PROFIT OR LOSS
cost_price = eval(input("Enter the cost price: "))
selling_price = eval(input("Enter the selling price: "))
if selling_price > cost_price:
    print("Profit is", selling_price - cost_price)
elif selling_price < cost_price:
    print("Loss is", cost_price - selling_price)
else:    
    print("No profit, no loss")


# EVEN OR ODD
number = eval(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# POSTIVE, NEGATIVE OR ZERO
number = eval(input("Enter a number: "))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")


# DIVISIBLE BY 3 AND 5
number = eval(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by both 3 and 5")


#SWAP TWO NUMBERS WITHOUT USING THIRD VARIABLE
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)


# VERIFY IF A NUMBER IS A LEAP YEAR OR NOT
year = eval(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


#MAXIMUM OF THREE NUMBERS
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
num3 = eval(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    print("The maximum number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The maximum number is:", num2)
else:
    print("The maximum number is:", num3)


# MINIMUM OF THREE NUMBERS
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
num3 = eval(input("Enter the third number: "))
if num1 <= num2 and num1 <= num3:
    print("The minimum number is:", num1)
elif num2 <= num1 and num2 <= num3:
    print("The minimum number is:", num2)
else:
    print("The minimum number is:", num3)


 # SUM OF MAXIMUM AND MINIMUM OF THREE NUMBERS
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
num3 = eval(input("Enter the third number: "))
maximum = max(num1, num2, num3)
minimum = min(num1, num2, num3)
sum = maximum + minimum
print("The sum of the maximum and minimum numbers is:", sum)


# ACCEPT MARKS OF 5 SUBJECTS AND CALCULATE TOTAL AND PERCENTAGE
sub1 = eval(input("Enter marks for subject 1: "))
sub2 = eval(input("Enter marks for subject 2: "))
sub3 = eval(input("Enter marks for subject 3: "))
sub4 = eval(input("Enter marks for subject 4: "))
sub5 = eval(input("Enter marks for subject 5: "))
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100
print("Total marks:", total)
print("Percentage:", percentage, "%")
