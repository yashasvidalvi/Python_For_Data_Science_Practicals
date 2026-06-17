#lambda
# new_marks2 = list(map(lambda m: m+5,marks))
# print(new_marks2)


# var = lambda a ,b :a if a>b else b
# print(var(10,20))

#from functools import reduce
# topperMarks = reduce(lambda a,b :a if a>b else b, marks)
# print(topperMarks)

# l = [[12,34],[32,54],[6,7]]
# sorted(l, key= lambda x : x[1])
# print(l)

# s = reduce(lambda a,b: a+b,[1,2,3,4,5])
# s1 = reduce(lambda a,b:a+b, [1,2,3,4,5], initial =s)

# print(s1)


# def addTwo(a,b):
#     return a+b

# res = addTwo(10,20)
# print(res)

#res = addTwo(10,20)
#print(res)

# def myDecorator(fun):
#     def wrapper():
#         print("*" *10)
#         print("=" *5)

#         print(fun(a,b))
#         print("="*5)
#         print("*"*10)
#     return wrapper

# wrapper = myDecorator(addTwo)
# wrapper(20,89)

def myDecorator(fun):
    def wrapper(a,b,c):
        s = fun(a,b)
        res1 = fun(s,c)
        #res = s+c
        return res1
    return wrapper

#addTwo = myDecorator(addTwo)
#r = addTwo(10,20,30)
#print(r)


@myDecorator
def addTwo(a,b):
    return a+b

r = addTwo(20,40,70)
print(r)
