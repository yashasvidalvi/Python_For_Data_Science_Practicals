# n = [10,10,25,31,40,50,40]

# total = 0
# for i in n:
#     total = total + i
# print(total)

# max = 0
# for i in n:
#     if i > max:
#         max = i
# print(max)

# min = n[0]
# for i in n:
#     if i < min:
#         min = i
# print(min)


# even = 0
# odd = 0
# for i in n:
#     if i % 2 == 0:
#         even +=1
#     else:
#         odd +=1
# print("Even:",even)
# print("Odd:",odd)

# reverse = []
# for i in range(len(n)-1,-1,-1):
#     reverse.append(n[i])
# print(reverse)


# new_list = []
# for i in n:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

# largest= n[0]
# second = n[0]

# for i in n:
#     if i >largest:
#         second = largest
#         largest = i
#     elif i>second and i != largest:
#         second = i
# print(second)

# freq = {}

# for i in n:
#     if i in freq:
#         freq[i]=freq[i]+1
#     else:
#         freq[i] = 1
# print(freq)

# t1 = (10,20,30,40)
# t2 = (10,30,50,60)

# list = []
# for i in t:
#     list.append(i)
# print(list)

# common = []

# for i in t1:
#     if i in t2:
#         common.append(i)
# print(common)

# t = (1,2,2,3,2,4)

# count = 0

# for i in t:
#     if i ==2:
#         count +=1
# print(count)

student ={
    "Math" : 50,
    "Physics":60,
    "Chemistry":70
}

# total = 0
# count = 0

# for i in student:
#     total = total+student[i]
#     count += 1

# average = total/count
# print(total)
# print(average)

highest = 0
subject = ""

for i in student:
    student[i] > highest
    highest = student[i]
    subject = i
print(subject)