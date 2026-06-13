#Task 1
#WAP to reverse given string
# def str_rev(s):

#     rev = ""
#     for ch in s:
#         rev = ch + rev
#     return rev
# s = "Python is Simple"
# rev = str_rev(s)
# print("Original String : ",s)
# print("Reverse String:",rev)

#Task 2
#WAP to reverse given string without changing word position
# def rev_words(s):
#     l = s.split()
#     rev = ""
#     for word in l:
#         rev = rev+" "+word[::-1]
#     return rev

# s = "Python is simple"
# print(rev_words(s))

#Task 3
#WAP to count total words in given string
s = "Python is funny programming language.I love it."
words = ["Python","is","funny","programming","language"]

def count_words(s):
    words = []
    w = ""
    for ch in s:
        if ch!=" " and ch!=".":
            w = w+ch
        elif ch==".":
            words.append(w)
            w = ""
        else:
            words.append(w)
            w=""
    return words,len(words)

l,count =count_words(s)
print(l)
print(count)
