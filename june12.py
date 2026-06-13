#Positional Arguments
# def addTwo(n1,n2):
#     print(n1)
#     print(n2)
#     return n1+n2
# addTwo(10,20)

#Keyword Argument
# def subTwo(n1,n2,n3):
#     print(n1)
#     print(n2)
#     print(n3)
#     return n1-n2-n3
# res = subTwo(n1 = 10,n2 = 20,n3 = 30)

#default argument
# def addThree(n1 = 0,n2 = 0,n3 = 0):
#     return n1+n2+n3
# res = addThree(n1=10,n2=20)
# print(res)

#Positional Arbitrary Arguments
# def Addition(*args):
#     print(args)
#     print(type(args))
#     r = sum(args)
#     return r
# s1 = Addition(10,20,30,40)
# s2 = Addition(10,20,30,40,50,60)

#Keyword Arbitrary Arguments
# def saveData(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# saveData(name = "Jay", mobile  = 8989789, pan = 1234)

#Task 1
#create a function that accepts any number of strings and return the longest string
def longest_string(*args):
    longest = args[0]
    for s in args:
        if len(s)>len(longest):
            longest = s
    return longest
print(longest_string("Python","Data Science","AI"))