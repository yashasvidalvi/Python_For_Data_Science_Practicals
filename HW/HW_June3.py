t = (1,2,3,[10,20],{7,8,9}) # we can add mutable data types like list and set to tuple but we cannot change them
print(t)
l = [10,20,(10,20),{1,2,3}] # we can add mutable data types like tuple and set to list but we cannot change them
print(l)
s ={10,20,(10,20),[4,5,6]} # we can add mutable data type like tuple but can't add list to set because list is mutable
print(s)
