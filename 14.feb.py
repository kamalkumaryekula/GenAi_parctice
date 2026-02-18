# 30. write a program to read positive numbers continuously until negative number is  
#given by using ‘if’. 

while True:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Negative number entered. Stopping.")
        break
    else:
        print("You entered:", num)

#output:
# Enter a number: 5
# You entered: 5
# Enter a number: 10
# You entered: 10
# Enter a number: -3
# Negative number entered. Stopping.


# 31.write a program to read ten numbers and print their sum by using ‘if’ statement. 

total = 0
count = 0

while count < 10:
    num = int(input(f"Enter number {count+1}: "))
    if num >= 0 or num < 0:   # condition ensures use of 'if'
        total += num
    count += 1

print("The sum of 10 numbers is:", total)

#output:
# Enter number 1: 5
# Enter number 2: 10
# Enter number 3: -3
# Enter number 4: 7
# Enter number 5: 2
# Enter number 6: 8
# Enter number 7: -1
# Enter number 8: 4
# Enter number 9: 6
# Enter number 10: 3
# The sum of 10 numbers is: 41

# 32.rite a program to read three sides a, b, c of a triangle and print the type of the triangle. 
# right angled triangle (a*a)+(b*b)==(c*c) || (b*b)+(c*c)==(a*a) || (c*c)+(a*a)==(b*b) 
# equilateral triangle (a==b) && (b==c) 
# isoceles triangle (a==b) || (b==c) || (c==a) 
# scalen (a! = b&&b!=c&& c!=a) 

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if (a*a + b*b == c*c) or (b*b + c*c == a*a) or (c*c + a*a == b*b):
    print("Right angled triangle")
elif a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or c == a:
    print("Isosceles triangle")
elif a != b and b != c and c != a:
    print("Scalene triangle")
else:
    print("Invalid triangle")

#output:
# Enter side a: 3
# Enter side b: 4
# Enter side c: 5
# Right angled triangle