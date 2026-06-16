#Higher order function
# def addTwo(a,b):
#     return a+b
# def MyHof(f1,p,q):
#     s = f1(p,q)
#     return s+10
# res = MyHof(addTwo,1,2)
# print(res)


marks = [67,98,88,76,34,91,79]
# grace_marks = []

# for m in marks:
#     grace_marks.append(m+5)
#     print(grace_marks)

#map function
# def add_5(m):
#     if m<90:
#         return m+5
#     else:
#         return m
# res = list(map(add_5,marks))
# print(res)

#filter function
# def greaterThan90(m):
#     if m>90:
#         return True
#     else:
#         return False
# topperlist = list(filter(greaterThan90,marks))
# print(topperlist)

def addTwo(a,b):
    return a+b
from functools import reduce 
s = reduce(addTwo,marks)
print(s)
