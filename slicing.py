##  string[start:end:step]


# 1. Simple Slicing
s = "Python Programming"
print(s[0:6])    # 'Python' → from index 0 to 5
print(s[7:18])   # 'Programming' → from index 7 to 17


# 2. Omitting Start or End
s = "Python Programming"
print(s[:6])     # 'Python' → start omitted
print(s[7:])     # 'Programming' → end omitted

# 3. Negative Indexing
s = "Python Programming"
print(s[-11:])   # 'Programming' → last 11 characters
print(s[:-11])   # 'Python' → everything except last 11


# 4. Step Parameter
s = "Python Programming"
print(s[::2])    # 'Pto rgamn' → every 2nd character
print(s[::3])    # 'Ph rgm'    → every 3rd character


# 5. Reversing a String
s = "Python Programming"
print(s[::-1])   # 'gnimmargorP nohtyP'


# 6. Slicing with Negative Step
s = "Python Programming"
print(s[17:6:-1])  # 'gnimmargorP' → backwards from index 17 down to 7


# 7. Full Dimensions Example
s = "Python Programming"
print(s[1:12:2])    # 'yhn rg' → from index 1 to 11, step 2
print(s[-17:-5:3])  # 'yo r'   → negative indices with step


# 8.Extract word "Programming":
s = "Python Programming"
print(s[s.index("P",7):])  # 'Programming'


# 9.Reverse words:
s = "Python Programming"
print(s[::-1])  # 'gnimmargorP nohtyP'

