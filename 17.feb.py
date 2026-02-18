# 36. write a program to read the characters continuously until ‘$’ is given and display the 
# number of characters entered. 

c = 0
while True:
    ch = input("Enter a character: ")
    if ch == "$":
        break
    c += 1

print("number of characters entered before $ is: " , c)

#output:
# Enter a character: k
# Enter a character: k
# Enter a character: l
# Enter a character: $
# number of characters entered before $ is:  3


# 37. Write a program to read a character and find out whether it is uppercase or lowercase. 

ch = input("Enter a character: ")

if 'A' <= ch <= 'Z':
    print("Uppercase letter")
elif 'a' <= ch <= 'z':
    print("Lowercase letter")
else:
    print("Not an alphabet character")

#output:

# Enter a character: k
# Lowercase letter
# Enter a character: J
# Uppercase letter
# Enter a character: 2
# Not an alphabet character


# 38. Write a program to print the uppercase letter of a given lowercase. 

ch = input("Enter a lowercase character: ")

if 'a' <= ch <= 'z':
    upper = chr(ord(ch) - 32)
    print("Uppercase is:", upper)
else:
    print("Not a lowercase character")


#output:
# Enter a lowercase character: k
# Uppercase is: K

# 39. write a program to check whether the given input is digit or lowercase character or 
#uppercase character or a special character (use ‘if-else-if’ ladder). 

ch = input("Enter a character: ")

if '0' <= ch <= '9':
    print("Digit")
elif 'a' <= ch <= 'z':
    print("Lowercase letter")
elif 'A' <= ch <= 'Z':
    print("Uppercase letter")
else:
    print("Special character")

#output:

# Enter a character: 2
# Digit
# Enter a character: l
# Lowercase letter
# Enter a character: A
# Uppercase letter
# Enter a character: #
# Special character


# 40. Do the above program by using ‘case’ statement. 

ch = input("Enter a character: ")

match ch:
    case ch if '0' <= ch <= '9':
        print("Digit")
    case ch if 'a' <= ch <= 'z':
        print("Lowercase letter")
    case ch if 'A' <= ch <= 'Z':
        print("Uppercase letter")
    case _:
        print("Special character")  

#output:

# Enter a character: 3
# Digit
# Enter a character: l
# Lowercase letter
# Enter a character: D
# Uppercase letter
# Enter a character: @
# Special character