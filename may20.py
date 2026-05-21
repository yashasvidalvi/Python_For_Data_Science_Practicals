# s = "Yashasvi"
# for ch in s:
#     print(ch)

# s = "Welcome to Python"
# count = 0
# for ch in s:
#     if ch == 'o':
#         count += 1
# print("Number of 'o' characters:", count)

#white space count in a string
# s = "I love Python programming."
# count = 0
# for ch in s:
#     if ch == ' ':
#         count += 1
# print("Total white spaces =", count)

#s = "Instagram"
# s1 = s[::-1]
# print("Original string:", s)
# print("Reversed string:", s1)

#String Methos

# print(s.upper())
# print(s.lower())
# print(s.startswith("Inst"))
# print(s.endswith("gram"))
# print(s.isalpha())
# print(s.isdigit())
# print(s.isalnum())
# print(s.isnumeric())

# s = "Student~name23~is~Jay~roll~nu32mber~is~45."

# l = s.split("~")
# print(l)

# s.join(l)

#print(len(s))

#count = 0
# for ch in s:
#     count = count + 1
# print("Total length =", count)

# v1 = "z"
# for ch in s:
#     if ch == v1:
#         count = count + 1
# print(f"Total number of characters {v1} in given string =", count)

s = input("Enter a string: ")
v1 = input("Enter a character to find count: ")
count = 0
for ch in s:
    if ch == v1:
        count = count + 1
print(f"Count of characters {v1} in given string =", count)
