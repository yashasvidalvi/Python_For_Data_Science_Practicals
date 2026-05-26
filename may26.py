#Task 1
# census_data = ['m','m','f','f','f','m','f','m','m','f','f','f','f']

# # count of male and female
# male = 0
# female = 0
# for gender in census_data:
#     if gender == 'm':
#         male = male + 1
#     else:
#         female = female + 1

# print("Male count:", male)
# print("Female count:", female)

# print("Total Male = ",census_data.count('m'))
# print("Total Female = ",census_data.count('f'))

#Task 2
name = ['Ajay', 'Priya','Pavan','Viru','Raj','Payal','Rohan']

#total count of names starting with P
# count = 0
# for n in name:
#     if n.startswith('P'):
#         count = count + 1
# print("Total names starting with P:", count)


#Task 3
#TOTAL COUNT OF STUDENTS WHOSE NAMES CONSIST OF TWO 'A'
# count = 0
# for n in name:
#     if n.lower().count('a') == 2:
#         count = count+1
# print("Total names with two 'a':", count)

total = 0
for n in name:
    count = 0
    for ch in n:
        if ch=='a' or ch=='A':
            count = count + 1
    if count == 2:
        total = total + 1
print("Total names with two 'a':", total)


