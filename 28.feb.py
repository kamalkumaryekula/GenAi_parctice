
# 80. Write a program to print the multiples of a given number upto 200. 

n = int(input("Enter a number: "))
i = 1
while n * i <= 200:
    print(n * i)
    i += 1

# output:
# Enter a number: 34
# 34
# 68
# 102
# 136
# 170

# 81.write a program to find the mean, variance and standard deviation of the given ‘n’ 
# numbers. 

n = int(input("Enter how many numbers: "))
nums = []

for i in range(n):
    val = float(input("Enter number: "))
    nums.append(val)

# Mean
sum_val = 0
for x in nums:
    sum_val += x
mean = sum_val / n


# Variance
var_sum = 0
for x in nums:
    var_sum += (x - mean) ** 2
variance = var_sum / n

# Standard Deviation
def sqrt(num):
    guess = num / 2
    for _ in range(20):  
        guess = (guess + num / guess) / 2
    return guess

std_dev = sqrt(variance)

print("Mean =", mean)
print("Variance =", variance)
print(f"Standard Deviation = {std_dev:.2f}")

# output:
# Enter how many numbers: 5
# Enter number: 11
# Enter number: 12
# Enter number: 13
# Enter number: 14
# Enter number: 15
# Mean = 13.0
# Variance = 2.0
# Standard Deviation = 1.41