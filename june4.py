set ={1,2,3,4,5}
fs = frozenset(set)
print(fs)

set.pop() #remvoe 1
remove = set.remove(3) #remove 3
print(set)

#level 0
student_db = {}
type(student_db)
roll = Name
student_db[5] ="Shreya"
student_db[2] ="Jay"
student_db[8] ="Rahul"
student_db[11] ="Priya"
print(student_db)
print(len(student_db))
print(student_db[5])

#key
print(student_db.keys())
roll=student_db.keys()
print(roll)
#value
print(student_db.values())
#items
print(student_db.items())

#how to iterate dictionary
#1st way
for key in student_db.keys():
    print(key)

for key in student_db:
    print(key)

#2nd way
for name in student_db.values():
    print(name)

for key in student_db:
    print(student_db[key])

#3rd way
for key in student_db:
    print(f"{key} : {student_db[key]}")

for t in student_db.items():
    print(t)

for roll,name in student_db.items():
#roll,name= t
    print(roll,name)

#print roll no of students whose name contains "y" in character
for roll,name in student_db.items():
    if "y" in name:
        print(roll)
