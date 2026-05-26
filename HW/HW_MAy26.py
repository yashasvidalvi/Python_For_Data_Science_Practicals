salary = [67000,45000,78000,55000,28000]

#2nd minimum salary
min_salary = salary[0]
for s in salary:
    if s < min_salary:
        min_salary = s
second_min = salary[0]
for s in salary:
    if s < second_min and s != min_salary:
        second_min = s
print(second_min)

#2nd maximum salary
max_salary = salary[0]
for s in salary:
    if s > max_salary:
        max_salary = s
second_max = salary[0]
for s in salary:
    if s > second_max and s != max_salary:
        second_max = s
print(second_max)
