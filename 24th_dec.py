
words = ['listen', 'silent', 'enlist', 'inlets', 'google', 'gooogle']
anagram_groups = {}
for word in words:
    sorted_word = "".join(sorted(word))
    if sorted_word in anagram_groups:
        anagram_groups[sorted_word].append(word)
    else:
        anagram_groups[sorted_word] = [word]
print(anagram_groups)

word = "kamal"
reversed_word = word[::-1]
sorted_ = "".join(sorted(word))
print(sorted_)

l = ["1.7",2.0,"5",6,8.6]
print([round(float(i)) for i in l])

# 
 