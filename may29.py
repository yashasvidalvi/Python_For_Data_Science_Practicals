#print negative numbers in the list

l = [45,-7,87,-67,45,33,-33,91,65,-56]

#print Start of for loop, start of if, end of if, end of for loop
# print("Start of for loop")
# for num in l:
#     print("Start of if")
#     if num < 0:
#         print(f"Negative Numbers are : {num}")
#     print("End of if")
# print("End of for loop")

#count of all even negative numbers
count = 0
for num in l:
    if num < 0 and num % 2 == 0:
        count += 1

print(f"Total Even Negative Numbers are : {count}")
