# 68.Write a program to find the factorial of the given number. 
num = int(input("Enter a number: "))
fact = 1
for i in range(1,num+1):
    fact *= i

print(f"Factorial of the given {num} is {fact}")

# output:
# Enter a number: 5
# Factorial of the given 5 is 120

# 69.Write a program to print all prime numbers from 1 to 99. 

for j in range(2, 100):   
    for i in range(2, j):
        if j % i == 0:  
            break
    else:
        print(j, end = " ")

# output:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97


# 70. Write a program to print the factorial prime from 1 to 99. 
fact = 1
for n in range(1,10):
    fact *= n
    for m in (fact-1,fact+1):
        if 1 < m < 100:
            for i in range(2,int(m*0.5)+1):
                if m % i ==0:
                    break
            else:
                print(m, end = " ")

# output:
# 2 3 5 7 23

# 71.Write a program to print Fibonacci series for a given number. 
a = 0
b = 1
num = int(input("Enter a number: "))
while a <= num:
    print(a,end = " ")
    a,b = b, a+b

# output:
# 0 1 1 2 3 5 8 13