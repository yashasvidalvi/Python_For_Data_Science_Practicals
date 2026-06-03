# varname = set()
# print(type(varname))

# s = set()
# s.add(10)
# s.add("sai")
# s.add(True)
# s.add("SAI")
# s.add(10+20j)
# t= (4,5,6)
# s.add(t)
# l= [7,8,9]
# #s.add(l)           # we cannot add list to set because list is mutable
# chotu_set ={3,4,5,6}
# #s.add(chotu_set)   # we cannot add set to set because set is mutable
# s.update((23, 45.5))
# print(len(s))
# print(s)

# s = {5,6,7,8}
# for ele in s:
#     print(s)
#Prove that set is mutable by code
# s = {1,2}
# address1 = id(s)
# print(address1)
# s.add(20.5)
# address2 = id(s)
# print(address2)
# if address1 == address2:
#     print("Set is Mutable.....")

# s1 = {1,2,3}
# s2 = {3,4,5}
# print(s1 |s2)
# print(s1 & s2)
# s3 = s1.intersection(s2)
# print(s3)
# s4 = s1.union(s2)
# print(s4)

# find common subjects between two students with lower case and upper case letters

student1 = ['Python', 'Java', 'SQL', 'HTML']
student2 = ['PHP', 'Python', 'React', 'JAVA']
# common_subjects = {s for s in student1 if s.lower() in {t.lower() for t in student2}}
# print(common_subjects)

for i in student1:
    for j in student2:
        if i.lower() == j.lower():
            print(i)