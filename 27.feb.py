# 77. Write a program to convert the given integer into binary and vice versa. 

# Convert integer to binary
num = int(input("Enter an integer: "))
binary_str = bin(num)[2:]   # remove '0b' prefix
print(f"Binary: {binary_str}")

# Convert binary back to integer
binary_input = input("Enter a binary number: ")
integer_val = int(binary_input, 2)
print(f"Integer: {integer_val}")

#output:
# Enter an integer: 10
# Binary: 1010
# Enter a binary number: 1111
# Integer: 15

# 78.Write a program to convert the given integer into octal. 

# Convert integer to octal
num = int(input("Enter an integer: "))
octal_str = oct(num)[2:]   # remove '0o' prefix
print(f"Octal: {octal_str}")

# Convert octal back to integer
octal_input = input("Enter an octal number: ")
integer_val = int(octal_input, 8)
print(f"Integer: {integer_val}")

#output:
# Enter an integer: 12
# Octal: 14
# Enter an octal number: 1111
# Integer: 585

# 79.Write a program to convert the given integer into hexadecimal. 

# Convert integer to hexadecimal
num = int(input("Enter an integer: "))
hex_str = hex(num)[2:].upper()   # remove '0x' prefix and uppercase
print(f"Hexadecimal: {hex_str}")

# Convert hexadecimal back to integer
hex_input = input("Enter a hexadecimal number: ")
integer_val = int(hex_input, 16)
print(f"Integer: {integer_val}")

# output:
# Enter an integer: 14
# Hexadecimal: E
# Enter a hexadecimal number: 1111
# Integer: 4369
