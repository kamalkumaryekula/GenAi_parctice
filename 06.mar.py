# 94.case conversions programs
text = "hello python world"

print("Original:", text)
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Capitalize:", text.capitalize())
print("Title:", text.title())
print("Swapcase:", text.swapcase())

# Original: hello python world
# Upper: HELLO PYTHON WORLD
# Lower: hello python world
# Capitalize: Hello python world
# Title: Hello Python World
# Swapcase: HELLO PYTHON WORLD


# 95.Removing Spaces Programs
text = "   Python Programming   "

print("Original:", text)
print("Strip:", text.strip())
print("Left Strip:", text.lstrip())
print("Right Strip:", text.rstrip())


# Original:    Python Programming
# Strip: Python Programming
# Left Strip: Python Programming
# Right Strip:    Python Programming


# 96 Searching Functions Programs
text = "python programming"

print("Find 'p':", text.find("p"))
print("Index 'g':", text.index("g"))
print("Count of 'm':", text.count("m"))
print("Starts with 'py':", text.startswith("py"))
print("Ends with 'ing':", text.endswith("ing"))

# Find 'p': 0
# Index 'g': 10
# Count of 'm': 2
# Starts with 'py': True
# Ends with 'ing': True


# 97.Replace / Modify Programs
text = "I like Java"

new_text = text.replace("Java", "Python")

print("Original:", text)
print("Modified:", new_text)

# Original: I like Java
# Modified: I like Python


# 98. Split & Join Programs
sentence = "Python is easy to learn"
words = sentence.split()

print(words)

# ['Python', 'is', 'easy', 'to', 'learn']



words = ["Python", "is", "powerful"]
sentence = " ".join(words)

print(sentence)
# Python is powerful

# 99.Checking Functions Programs
text = "Python123"

print(text.isalnum())
print(text.isalpha())
print(text.isdigit())
print(text.islower())
print(text.isupper())

# True
# False
# False
# False
# False

# 100. Email validation example
email = "user@gmail.com"

if email.endswith("@gmail.com"):
    print("Valid Gmail account")
else:
    print("Invalid email")

# Valid Gmail account
