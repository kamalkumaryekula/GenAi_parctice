# 46. write a program to read your name and print it ‘n’ times. 
name = input("Enter your name: ")
n = int(input("Enter how many times to print: "))

for i in range(n):
    print(name)

# output:
# Enter your name: kamal
# Enter how many times to print: 3
# kamal
# kamal
# kamal

# 47. Write a program to find whether the given numbers existing in an array or not. 
arr = [10, 20, 30, 40, 50]
num = int(input("Enter a number to search: "))

if num in arr:
    print(f"{num} exists in the array.")
else:
    print(f"{num} does not exist in the array.")

# output:
# Enter a number to search: 30
# 30 exists in the array.

# 48.Write a program to find the sum of ‘n’ natural numbers. 
n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum of first", n, "natural numbers is:", total)

# output:
# Enter n: 15
# Sum of first 15 natural numbers is: 120

# 49. Write a program to find the sum of ’n’ distinct numbers. 
n = int(input("Enter how many numbers: "))
numbers = set()  # ensures distinct values

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.add(num)

print("Sum of distinct numbers is:", sum(numbers))

# output:
# Enter how many numbers: 5
# Enter number 1: 23
# Enter number 2: 63
# Enter number 3: 45
# Enter number 4: 96
# Enter number 5: 12
# Sum of distinct numbers is: 239

# 50. Write a program to find the sum of even ‘n’ natural numbers. 
n = int(input("Enter n: "))
total = 0

for i in range(2, 2*n + 1, 2):  # even numbers up to 2n
    total += i

print("Sum of first", n, "even natural numbers is:", total)

# output:
# Enter n: 20
# Sum of first 20 even natural numbers is: 420