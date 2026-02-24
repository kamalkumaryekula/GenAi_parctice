# 64. Write a program to find the sum and product of the individual digits of a given number. 
num = int(input("Enter a number: "))
temp = num
s_d = 0
p_d = 1

while temp > 0:
    digit = temp % 10
    s_d += digit
    p_d *= digit
    temp //= 10

print(f"Sum of digits of {num} is {s_d}")
print(f"Product of digits of {num} is {p_d}")

# output:
# Enter a number: 256
# Sum of digits of 256 is 13
# Product of digits of 256 is 60

# 65. Write a program to accept maximum of 6 digits number and find out the sum of even 
# digits of that number and multiplication of odd digits of that number. 
num = int(input("Enter a 6 digit number: "))
s_d = 0
m_d = 1
for i in str(num):
    digit = int(i)
    if digit %2 ==0:
        s_d += digit
    else:
        m_d *= digit
    
print(f"Sum of even digits in {num} is {s_d}")
print(f"Multiplication  of odd digits in {num} is {m_d}")

# output:
# Enter a 6 digit number: 369852
# Sum of even digits in 369852 is 16
# Multiplication  of odd digits in 369852 is 135


# 66.Write a program to find the number of digits of a given number. 
num =int(input("Enter a number: "))
c = 0
for i in str(num):
    c += 1

print("No of digits in a number", c)

# output:
# Enter a number: 258936
# No of digits in a number 6

# 67.Write a program to print the reverse of a given number. 

num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    d = temp % 10
    rev = rev *10 +d
    temp //=10

print("Reverse of the number is:",rev)

# output:
# Enter a number: 369
# Reverse of the number is: 963