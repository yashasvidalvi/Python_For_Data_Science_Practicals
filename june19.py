# a = [12,34,6,8,9]

#sum , average
# total = 0
# count = 0
# for i in a:
#     total = total + i
#     count = count +1
# average = total/count
# print(total)
# print(average)


students = {
    "ram":"60",
    "shyam":"90",
    "laxman":"30",
    "sita":"130",
    "hanuman":"130"
}

#sum , average
# total = 0
# count = 0

# for name, marks in students.items():
#     total = total+ int(marks)
#     count = count + 1
# average = total / count
# print(total)
# print(average)


#max marks
# max_marks = 0
# max_name = ""
# for name, marks in students.items():
#     if int(marks)>max_marks:
#         max_marks = int(marks)
#         max_name = name
# print(max_marks)
# print(max_name)


# input name and print marks

# person = input("Enter name:")

# for name, marks in students.items():
#     if name == person:
#         print(marks)

#count of people of marks 130

# count = 0 
# for name in students:
#     if int(students[name]) == 130:
#         count += 1
# print(count)

#increase marks by 10
# l2 ={}
# for name in students:
#     marks = int(students[name])
#     marks = marks + 10
#     l2[name] = str(marks)
# print(l2)


#reduce marks by 20 if found "am" in name
l2 = {}
for name in students.keys():
    if "am" in name:
        marks = int(students[name])
        marks = marks - 20
        l2[name] = str(marks)
print(l2)
