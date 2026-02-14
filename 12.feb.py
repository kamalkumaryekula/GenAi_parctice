# 23.Write a program to read the marks of 3 subjects and display the total, avg, class. 

m1 = int(input("Enter marks of subject 1: "))   #84
m2 = int(input("Enter marks of subject 2: "))   #94
m3 = int(input("Enter marks of subject 3: "))   #89

total = m1 + m2 + m3
avg = total / 3

print("Total =", total)                 #267
print(f"Average = {avg:.2f}")           #89.00

if avg >= 60:
    print("Class = First")
elif avg >= 50:
    print("Class = Second")
elif avg >= 35:
    print("Class = Pass")
else:
    print("Class = Fail")

#output:
#Class = First

# 24.Write a program to check whether the given number is positive or negative. 
num = int(input("Enter a number: "))  #6

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#output:
#Positive

# 25.Write a program to find out the given number is odd or even. 
num = int(input("Enter a number: "))    #25

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#output:
#Odd

# 26.Write a program to find smallest of given two numbers. 

a = int(input("Enter first number: "))  #10
b = int(input("Enter second number: ")) #15

if a < b:
    print("Smallest =", a)
elif b < a:
    print("Smallest =", b)
else:
    print("Both are equal")


#output:
#Smallest = 10