#closure
# def f1(x):
#     def f2(y):
#         return x*y
#     return f2

# v1 = f1(10)
# v2 = f1(100)
# v3 = f1(200)
# v4 = f1(400)

# print("We are inside Global scope")
# print("I am calling f2 function from global scope")
# print(v1(20))
# print(v2(20))

# print(v1(50))
# print(v2(50))

#closure
# def f1(x):
#     def f2(y):
#         def f3(z):
#             return x+y+z
        
#         return f3
#     return f2

# f2 = f1(10)
# f3 = f2(20)
# res = f3(30)
# print(res)


l = [5,9,7,8,99,0]
p = [5,8,4,7]
#Task 1
# for num in l:
#     if num % 2 ==0:
#         print(num)

#Task 2

# for num in l:
#     if num >10:
#         print(num)

#Task 3
l.extend(p)
print(l)

#Task 4
x = set(l)
print(x)

#Task 5
total = sum(l)+sum(p)
print(total)

#count no of even odd
even = 0
odd = 0
for num in l:
    if num % 2==0:
        even+=1
    else:
        odd+=1
print(l)
print(even)
print(odd)