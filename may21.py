# l = []
# #print(type(l))

# l.append(10)
# l.append(20.5)
# l.append("Diksha")
# l.append(True)
# l.append(10)
# l.append("Diksha")
# print(len(l))
# print(l[3: ])


Students_Name = ["Yashasvi", "Diksha", "Satyarth", "Shivam", "Anshul","Shreya","Siya","Gita","Sita","Rama"]

# Find Total number of students in the class whose name size is 4 
count = 0
for name in Students_Name:
    if len(name) == 4:
        count += 1
print("Total number of students in the class whose name size is 4 only:", count)

# #print("Total number of students in the class:", len(Students_Name))

