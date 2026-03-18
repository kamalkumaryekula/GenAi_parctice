# Write a program to read a line of text and find the number of words when the words 
#are separated by more than one space. 

s = input("Enter text: ")
ss = list(s.split())            # split automatically counts double spaces.
print(ss)
print(len(ss))



# Write a program to read a line of text and find the words which are occurred more than once.
s = input("Enter context: ")
ss = s.split()
print(ss)
l = []
for i in ss:
    if i not in l:
        l.append(i)

print(l)



from collections import Counter

s = input("Enter text: ")
words = s.split()
counts = Counter(words)


print(counts)
print("Words occurring more than once:")
for w, count in counts.items():
    if count > 1:
        print(f"{w} -> {count} times")
