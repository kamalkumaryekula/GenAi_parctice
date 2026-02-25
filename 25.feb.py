# 72.Write a program to find ‘n’ power ‘n’ (nn). 

n = int(input("Enter a number: "))
result = 1
for i in range(n):
    result *= n

print(f"The Result is {result}")

# output:
# Enter a number: 5
# The Result is 3125

# 73.Write a program to find ‘m’ power ’n’ (mn). 

m = int(input("Enter Base value : "))
n = int(input("Enter Power value : "))
result = 1
for i in range(n):
    result *= m

print(f"The result is {result}")

# output:
# Enter Base value : 2
# Enter Power value : 5
# The result is 32


# 74.Write a program to find ‘m’ power ‘n’ value without using (*). 
m = int(input("Enter value of m: "))

n = int(input("Enter value of n: "))

result = 1
for i in range(n):
    temp = 0
    for j in range(m):
        temp += result
    result = temp

print("The result is", result)

# output:
# Enter value of m: 2
# Enter value of n: 5
# The result is 32
