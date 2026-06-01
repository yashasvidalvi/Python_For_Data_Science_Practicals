#for loop use
# for i in range(1,6):
#     print(i)

# #while loop use
# num =1
# while num <= 5:
#     print(num)
#     num += 1
# print(num)

# #DRY Run
# num =1
# while num <= 5:
#     num += 1
#     print(num)
#     num += 1

# num =1
# while num <= 5:
#     num += 1
#     print(num)
#     num -= 2

num =2113
count = 0
while num > 0:
    num = num // 10
    count += 1
print(count)
