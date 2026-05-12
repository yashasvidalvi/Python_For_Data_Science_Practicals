roll = 111
name ="Jay"
per = 90.54

# f string method
# print("-"*25)
# print("|Roll |Name |Percentage|")
# print("-"*25)
# s1 = len("Rahul")
# print(f"|{roll:<4} |{name:^4} |{per:>10}|")
# print("-"*25)

#print("Student Roll No is "+str(roll)+" and Name is "+name+".")
# #s = f"Student Roll No is {roll} and Name is {name}."
# #s = "Student Roll No is "+str(roll)+" and Name is "+name+"."
# s = f"Student Roll is {roll:03d} and Name is {name} and percentage is {per:.2f}."
# print(s)

# filename = input("Enter the file name: ")
# path = f"C:/Users/HP/Desktop/{filename}"
# print(path)

# arr = [23,45,67,89,12,34]
# print(max(arr))

# .format method 

# s = f"Student roll is {roll:03d} name is {name} and percentage is {per:3f}."
# print(s)

# s2 = "Student roll is {} name is {} and percentage is {}.".format(roll,name,per)
# print(s2)

# s3 = "Student roll is {0} name is {1} and percentage is {2}.".format(roll,name,per)
# print(s3)

# s4 = "Student roll is {v1} name is {v2} and percentage is {v3}.".format(v1=roll,v2=name,v3=per)
# print(s2)

#.% method 

s5 = "Student roll is %d name is %s and percentage is %f."%(roll,name,per)
print(s5)