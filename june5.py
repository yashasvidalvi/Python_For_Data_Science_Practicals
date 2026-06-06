#create a dictionary to store 5 movie name and its cast

movies_db = {
    "Dhurandhar": ["Ranveer Singh", "Akshay Khanna", "Sanjay Dutt", "Sara Arjun"],
    "Jawan": ["Shah Rukh Khan", "Nayanthara", "Vijay Sethupathi"],
    "Animal": ["Ranbir Kapoor", "Rashmika Mandanna", "Anil Kapoor"],
    "Pushpa": ["Allu Arjun", "Rashmika Mandanna", "Fahadh Faasil"],
    "KGF": ["Yash", "Shrinidhi Shetty", "Sanjay Dutt"]
}

# print("Movies Database:", movies_db)

#Task 1
#display the names of movies one by one from your movies db

# for movie in movies_db.keys():
#     print(movie)

#Task 2
#Display movie name who is having Akshay Khanna in his cast

# for movie, cast in movies_db.items():
#     if "Akshay Khanna" in cast:
#         print(movie)

#Task 3
#Find the count of actor/actress names per movie whose name has more than 15 characters

# for movie, cast in movies_db.items():
#     count = 0
#     cast_names = []
#     for actor in cast:
#         if len(actor) > 15:
#             count += 1
#             cast_names.append(actor)
#     if count > 0:
#         print(f"{movie} : {count} {' '.join(cast_names)}")

#second way
# length_of_char =15
# for movie, cast in movies_db.items():
#     count = 0
#     for name in cast:
#         if len(name) > length_of_char:
#             count += 1
#     print(f"{movie} : {count}")

#Task 4
#Find  frequency of every actor/actress in your movies db and print it
frequency = {}
for movie, cast in movies_db.items():
    for actor in cast:
        if actor in frequency:
            frequency[actor] += 1
        else:
            frequency[actor] = 1

print("Actor Frequency:")
for actor, count in frequency.items():
    print(f"{actor}: {count}")

#Task 5: Find frequency of every character in a string and print it
# s = "i love python programming "

# frequency = {}
# for char in s:
#     key = char
#     value = s.count(char)
#     frequency[key] = value
# print(frequency)

