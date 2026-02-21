# 59. write a program to check given number is prime or not.
num = int(input("Enter a number: "))

if num <= 1:
    print("It is not a prime number")
else:
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")


# output:
# Enter a number: 9
# it is not a prime number

# 60. write a program to check given number is perfect or not.

num = int(input("Enter a number: "))
sum_div = 0

for i in range(1, num):
    if num % i == 0:
        sum_div += i

if sum_div == num:
    print("It is a Perfect number")
else:
    print("It is not a Perfect number")

# output:
# Enter a number: 6
# It is a Perfect number


# 61.Write a program to find the given number is automorphic or not. 
num = int(input("Enter a number: "))
square = num * num

if str(square).endswith(str(num)):
    print("It is an Automorphic number")
else:
    print("It is not an Automorphic number")

# output:
# Enter a number: 25
# It is an Automorphic number


# 62. Write a program to find the given number is Armstrong or not. 
num = int(input("Enter a number: "))
temp = num
power = len(str(num))
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit ** power
    temp //= 10

if sum_digits == num:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")

# output:
# Enter a number: 153
# It is an Armstrong number



# 63. Write a program to find the given number is palindrome or not. 
num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if rev == num:
    print("It is a Palindrome number")
else:
    print("It is not a Palindrome number")

# output:
# Enter a number: 121
# It is a Palindrome number