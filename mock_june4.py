# l = [1, 2, 3, 4, 5, 1, 2, 3]
# l = list(set(l))
# print(l)


#how to add forcefully elements in tuple
t = (1,2,3,4,5)
l = list(t)
l.append(10)
t = tuple(l)
print(t)