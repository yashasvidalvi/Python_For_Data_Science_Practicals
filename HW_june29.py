#Use of dunder methods
class Book:
    def __init__(self,t,p):
        self.title = t
        self.price = p
    
    def __add__(self, other):
        return self.price+other.price
    def __sub__(self, other):
        return self.price - other.price
    def __mul__(self, other):
        return self.price * other.price
    def __truediv__(self, other):
        return self.price / other.price
    def __floordiv__(self, other):
        return self.price // other.price
    def __mod__(self, other):
        return self.price % other.price
    def __pow__(self, other):
        return self.price ** other.price
    def __lt__(self, other):
        return self.price < other.price
    def __le__(self, other):
        return self.price <= other.price
    def __gt__(self, other):
        return self.price > other.price
    def __ge__(self, other):
        return self.price >= other.price
    def __eq__(self, other):
        return self.price == other.price
    def __ne__(self, other):
        return self.price != other.price
    def __iadd__(self, other):
        self.price += other.price
        return self
    def __isub__(self, other):
        self.price -= other.price
        return self

b1 = Book("Core Python ", 250)
b2 = Book("Data Analytics", 450)
print(b1 + b2)
print(b1 - b2)
print(b1 * b2)
print(b1 / b2)
print(b1 // b2)
print(b1 % b2)
print(b1 ** b2)
print(b1 < b2)
print(b1 <= b2)
print(b1 > b2)
print(b1 >= b2)
print(b1 == b2)
print(b1 != b2)

b1 += b2
print(b1.price)
b1 -= b2
print(b1.price)



# addition of three numbers
class Book:
    def __init__(self,t,p):
        self.title = t
        self.price = p
    
    def __add__(self, other):
            return Book("",self.price + other.price)
    

b1 = Book("Core Python ", 250)
b2 = Book("Data Analytics", 450)
b3 = Book("Machine Learning", 500)

print((b1 + b2).price)      
print((b1 + b2 + b3).price) 