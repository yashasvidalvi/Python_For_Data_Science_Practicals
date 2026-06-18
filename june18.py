students = {
    101:{"phy":40, "che":56, "math":78},
    102:{"phy":60,"che":65,"math":58},
    103:{"phy":50,"che":76,"math":56}
}
#Average
# print(students[101])
# total_phy_marks = 0
# total_phy_count = 0
# for rollnumber,marks_sub in students.items():
#     total_phy_marks = total_phy_marks+marks_sub["phy"]
#     total_phy_count = total_phy_count+1

#     print(total_phy_marks/(total_phy_count))

# total_che_marks = 0
# total_che_count = 0
# for rollnumber,marks_sub in students.items():
#     total_che_marks = total_che_marks + marks_sub["che"]
#     total_che_count = total_che_count + 1

# print(total_che_marks/(total_che_count))


# print(students[101])
# total_math_marks = 0
# total_math_count = 0
# for rollnumber,marks_sub in students.items():
#     total_math_marks = total_math_marks+marks_sub["math"]
#     total_math_count = total_math_count+1

#     print(total_math_marks/(total_math_count))


#sum percentage
rollno = int(input("Enter Roll Number: "))

if rollno in students:
    marks = students[rollno]

    total = marks["phy"] + marks["che"] + marks["math"]
    percentage = (total / 300) * 100

    print("Roll No:", rollno)
    print("Total Marks:", total)
    print("Percentage:", round(percentage, 2), "%")
else:
    print("Roll Number not found")