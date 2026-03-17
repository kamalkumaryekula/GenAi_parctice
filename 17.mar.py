# # find the occurance of a character in a given string
# s = input("Enter a string: ")

# # Dictionary to store character counts
# char_count = {}

# for c in s:
#     if c in char_count:
#         char_count[c] += 1
#     else:
#         char_count[c] = 1

# print((char_count))




# # palindrome checck.
# s = input("Enter a string: ")
# if s == s[::-1]:
#     print("palindrome")
# else:
#     print("Not a palindrome")



# # Write a program to read ‘n’ names and print it in ascending order. 
# n = int(input("Enter a number: "))
# names = []
# for i in range(n):
#     name = input(f"Enter name{i+1} is: ")
#     names.append(name)

# names.sort()

# for name in names:
#     print(name)


# # 186.   Write a program to read ‘n’ names and print the distinct names. 
# n = int(input("Enter a number: "))
# names = []
# for i in range(n):
#     name = input(f"Enter name{i+1} is: ")
#     names.append(name)

# distinct_names = set(names)

# print(distinct_names)


# # Write a program to read ‘n’ names and print the names which are occurred more than once.

# # Program to read 'n' names and print names that occurred more than once

# n = int(input("Enter how many names: "))
# names = []

# # Read names
# for i in range(n):
#     name = input(f"Enter name {i+1}: ")
#     names.append(name)

# # Find duplicates
# print("\nNames that occurred more than once:")
# duplicates = set()  # to store repeated names
# for name in names:
#     if names.count(name) > 1:
#         duplicates.add(name)

# # Print results
# # if duplicates:
# if duplicates:
#     for name in duplicates:
#         print(name)
# else:
#     print("No names occurred more than once.")



# replacing the substring with newone.
# s = "Kamal is a hardworking student who always focuses on learning new skills."
# ss = list(s.split())
# print(ss)
# rs = input("Enter a string that want to replace: ")
# new_word = input("Enter a string: ")
# for i in range(len(ss)):
#     if ss[i] == rs:
#         ss[i] = new_word


# re = " ".join(ss)
# print(f"updated string: {re}")



# 190.   Write a program to read a line of text and find the number of blank spaces. 
line = input("Enter a line of text: ")
space_count = line.count(" ")
print(f'number of blank spaces: {space_count}')



# 191.   Write a program to read a line of text and find the number of words. 
words = line.split()
print(f"Number of Words: {len(words)}")



# Write a program to read a line of text and find the number of words when the words 
# are separated by more than one space.