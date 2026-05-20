# count vowels in a string
s = "Yashasvi"
vowel_count = 0
for ch in s:
    if ch in 'aeiouAEIOU':
        vowel_count += 1    
print("Number of vowels in the string:", vowel_count)