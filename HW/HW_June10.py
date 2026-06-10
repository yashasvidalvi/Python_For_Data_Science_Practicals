
#global scope
x = 10
def f1():
    #local scope
    x =20
    print(x)
f1()
print(x)