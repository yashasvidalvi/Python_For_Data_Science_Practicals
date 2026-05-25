l1 = [1,2,3]
l2 = [5,6,7]
print(l1+l2)
print(l1*3)

#Total salary 
salary = [67000,45000,78000,55000,28000]
total = salary[0]+ salary[1]+salary[2]+salary[3]+salary[4]
print(total)

# total = 0
for s in salary:
    total = total + s  
print(total)

#sum of odd index salary from given list
#Method 1
total = 0
for i in range(1,len(salary),2):
    total = total + salary[i]
print(total)

# #Method 2
total = 0
for i in range(len(salary)):
    if i%2 == 1:
        total = total + salary[i]
print(total)

# sum of first half of the list employees salary
total = 0
for i in range(len(salary)//1):
    total = total + salary[i]
print(total)

# half = len(salary)//2
total = 0
for i in range(half,len(salary)):
    total = total + salary[i]
print(total)

# s = "Instagram"
half = len(s)//2
t = 0
for i in range(len(s)//2):
    t = t+salary[i]
print(t)

# sum of first half of the string
s = "Instagram"
half = len(s)//2
total = s[0:half]
print(total)