# 27.Write a program to find biggest of given three numbers. 

a = int(input("Enter value of A: "))    #56
b = int(input("Enter value of B: "))    #25
c = int(input("Enter value of c: "))    #36

if a > b and a > c:
    biggest = a
elif b > a and b > c:
    biggest = b
else:
    biggest = c

print(f'Biggest of three numbers is {biggest}')

#output:
#Biggest of three numbers is 56


# 28.Write a program to check whether the given year is leap year or not. 

year = int(input("Enter a year: ")) #2024

if (year%100 != 0 and year%4 == 0) or year %400 == 0:
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year. ')


#output:
#2024 is a leap year.


# 29.Write a program to find the roots of a given quadratic equation and
#  print the nature of roots.

# Quadratic equation: ax^2 + bx + c = 0

a = float(input("Enter coefficient a: "))   #5
b = float(input("Enter coefficient b: "))   #2
c = float(input("Enter coefficient c: "))   #7

# Calculate discriminant
d = b**2 - 4*a*c

print(f"Discriminant = {d}")

if d > 0:
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print("Roots are real and distinct.")
    print(f"Root 1 = {root1}, Root 2 = {root2}")
elif d == 0:
    root = -b / (2*a)
    print("Roots are real and equal.")
    print(f"Root = {root}")
else:
    realPart = -b / (2*a)
    imagPart = ((-d)**0.5) / (2*a)
    print("Roots are complex and conjugate.")
    print(f"Root 1 = {realPart} + {imagPart}i")
    print(f"Root 2 = {realPart} - {imagPart}i")

#output:
# Discriminant = -136.0
# Roots are complex and conjugate.
# Root 1 = -0.2 + 1.1661903789690602i
# Root 2 = -0.2 - 1.1661903789690602i
