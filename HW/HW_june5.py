movies_db = {
    "Dhurandhar": ["Ranveer Singh", "Akshay Khanna", "Sanjay Dutt", "Sara Arjun"],
    "Jawan": ["Shah Rukh Khan", "Nayanthara", "Vijay Sethupathi"],
    "Animal": ["Ranbir Kapoor", "Rashmika Mandanna", "Anil Kapoor"],
    "Pushpa": ["Allu Arjun", "Rashmika Mandanna", "Fahadh Faasil"],
    "KGF": ["Yash", "Shrinidhi Shetty", "Sanjay Dutt"]
}

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
    