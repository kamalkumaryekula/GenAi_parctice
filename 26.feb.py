# 75. Write a program to find the G.C.D. of ‘n’ numbers. 

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

while b !=0:
    temp = b
    b = a%b
    a = temp

print("GCD of a and b is:",a)

# output:
# Enter value of a: 12
# Enter value of b: 18
# GCD of a and b is: 6


# 76.Write a program to find the L.C.M. of ‘n’ numbers. 
a = int(input("Enter value of a: "))
b = int(input("Enter a number: "))

x,y = a, b
while y !=0:
    temp = y
    y = x%y
    x = temp

gcd = x
lcm = abs(a*b)//gcd
print(f"LCM of {a} and {b} is {lcm}")

# output:
# Enter value of a: 20
# Enter a number: 30
# LCM of 20 and 30 is 60

