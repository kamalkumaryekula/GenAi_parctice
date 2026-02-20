# 41. write a program to read a vowel character and print any appropriate word by using “case”

vowel = input("Enter a vowel (a, e, i, o, u): ").lower()

match vowel:
    case "a":
        print("Apple")
    case "e":
        print("Elephant")
    case "i":
        print("Icecream")
    case "o":
        print("Orange")
    case "u":
        print("Umbrella")
    case _:
        print("Not a vowel")

# output:
# Enter a vowel (a, e, i, o, u): i
# Icecream

# 42.Write a program to find the biggest number among 2 numbers by using case. 
      
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

match (a > b, a < b):
    case (True, False):
        print(f"{a} is bigger")
    case (False, True):
        print(f"{b} is bigger")
    case _:
        print("Both are equal")

# output:
# Enter first number: 12
# Enter second number: 13
# 13 is bigger


# 43. write a program to emulate a four function calculator which can perform addition, 
# subtraction, multiplication and division. Program should read two real numbers and an 
# operator which tells the operation to be performed. Do it by using case. 

num1 = float(input("Enter first number: "))         
num2 = float(input("Enter second number: "))        
op = input("Enter operator (+, -, *, /): ")

match op:
    case "+":
        print("Result:", num1 + num2)   
    case "-":
        print("Result:", num1 - num2)   
    case "*":
        print("Result:", num1 * num2)   
        if num2 != 0:
            print("Result:", num1 / num2)   
        else:
            print("Division by zero not allowed")  
    case _:
        print("Invalid operator")   
# output:
# Enter first number: 12
# Enter second number: 13
# Enter operator (+, -, *, /): *
# Result: 156.0 


# 44.Write a program to accept a date and print it in words by using case. 

d = int(input("Day: "))
m = int(input("Month: "))
y = int(input("Year: "))

match m:
    case 1: print(d, "January", y)
    case 2: print(d, "February", y)
    case 3: print(d, "March", y)
    case 4: print(d, "April", y)
    case 5: print(d, "May", y)
    case 6: print(d, "June", y)
    case 7: print(d, "July", y)
    case 8: print(d, "August", y)
    case 9: print(d, "September", y)
    case 10: print(d, "October", y)
    case 11: print(d, "November", y)
    case 12: print(d, "December", y)
    case _: print("Invalid month")


# output:
# Day: 15
# Month: 11
# Year: 2001
# 15 Nov 2001



# 45. write a program to read a number and print how many numbers of 500, 100, 20, 10, 
# 5,2,1 notes are available in the given amount by using case.

amount = int(input("Enter the amount: "))   #684

match amount:
    case _:
        notes500 = amount // 500
        amount %= 500

        notes100 = amount // 100
        amount %= 100

        notes20 = amount // 20
        amount %= 20

        notes10 = amount // 10
        amount %= 10

        notes5 = amount // 5
        amount %= 5

        notes2 = amount // 2
        amount %= 2

        notes1 = amount // 1

print("500 notes =", notes500)      #1
print("100 notes =", notes100)      #1
print("20 notes =", notes20)        #4
print("10 notes =", notes10)        #0
print("5 notes =", notes5)          #0
print("2 notes =", notes2)          #2
print("1 notes =", notes1)          #0


