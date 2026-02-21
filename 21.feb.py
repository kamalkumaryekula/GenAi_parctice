# 55. Write a program to find the biggest of the given numbers. 

numbers = [12, 45, 7, 89, 23]
biggest = numbers[0]
for n in numbers:
    if n > biggest:
        biggest = n
print("Biggest number:", biggest)

# output:
# Biggest number: 89


# 56 .Write a program to find the second smallest number and its position among the given 
# ‘n’ numbers. 
numbers = [12, 45, 7, 89, 23]

# Step 1: Find the smallest number
smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n

# Step 2: Find the second smallest (greater than smallest)
second_smallest = None
for n in numbers:
    if n != smallest:  # skip the smallest itself
        if second_smallest is None or n < second_smallest:
            second_smallest = n

# Step 3: Find position (1-based index)
position = -1
for i in range(len(numbers)):
    if numbers[i] == second_smallest:
        position = i + 1
        break

print("Second smallest:", second_smallest, "at position", position)

# output:
# Second smallest: 12 at position 1



# 57. Write a program to find the total number of +ve numbers, -ve numbers and zeros out 
# of a given 10 real numbers.
numbers = [5, -3, 0, 12, -7, 0, 9, -1, 4, 0]
positive = 0
negative = 0
zeros = 0

for n in numbers:
    if n > 0:
        positive += 1
    elif n < 0:
        negative += 1
    else:
        zeros += 1

print("Positives:", positive, "Negatives:", negative, "Zeros:", zeros)

# output:
# Positives: 4 Negatives: 3 Zeros: 3

# 58.Write a program to print the numbers which are divisible by both 3 and 7 from 1 to 100. 

for i in range(1, 101):
    if i % 3 == 0 and i % 7 == 0:
        print(i)

# output:
# 21
# 42
# 63
# 84