# Read mode

#  file_path = "demo.txt"
# m = "r"
# fh = open(file_path,mode = m)
# print("File open successfully in read mode")
# data = fh.readlines()
# print(data[1])
# fh.close()
# print("File close successfully in read mode")

# with open(file_path,mode = m) as fh:
#     print("File open successfully in read mode")
#     data = fh.readlines()
#     print(data[1])
#     fh.close()
# print("File close successfully in read mode")

# Write Mode

# file_path = "demo1.txt"
# m = "r"
# m1 = "w"
# m2 = "a"
#m3 = "x"

# with open(file_path, mode = m3) as fh:
#     print("File opened successfully in exclusive creation mode")

# with open(file_path, mode = m2) as fh:
#     print("File opened successfully in append mode")
#     fh.write("This is a demo file\n")
# with open(file_path,mode = m1) as fh:
#     print("File open successfully in write mode")
#     fh.write("This is a demo file\n")
#     fh.write("This is second line\n")
#     fh.write("This is third line\n")
#     fh.write("This is fourth line\n")
# print("FIle closed successfully")


# file_path = "Yashasvi_Photo.jpg"
# file_path2 = "Yashasvi_Photo_Copy.jpg"
# m1 = "rb"
# m2 = "wb"

# with open(file_path,mode = m1) as fh, open(file_path2, mode = m2) as fh1:
#     print("File open successfully in read mode")
#     data = fh.read()
#     fh1.write(data)
# print("FIle closed successfully")