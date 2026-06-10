# Task 1
#by using list
# def find_topper(student_data):
#      t = max(student_data)
#      return t

# #by using dictionary
# def find_topper(student_data):
#     n = ""
#     t = 0

#     #t = students_data[0]
#     for name, marks in student_data.items():
#         if marks>t:
#             t = marks
#             n = name
#     return n,t

# students = {"Yashasvi":90,"Asmita":56,"Diksha":87,"Shreya":78}
# l = [69,91,82,99,88,67,33,45]

# topper_name , topper_marks = find_topper(students)
# print("Topper Name is :",topper_name)
# print("Topper marks is :",topper_marks)

#Task 2

l = ['jay@gmail,com','raj@gmail.com','pavan@gmail.com','raj@gmail.com','jay@gmail,com','jay@gmail,com']

def delete_duplicates_email(email_list):
    unique_emails =set(email_list)
    print("Unique email is :",unique_emails)
    count = 0
    for email in unique_emails:
        count = email_list.count(email)
        count = count -1 
        print(f"{email} need to delete {count} times")

delete_duplicates_email(l)
