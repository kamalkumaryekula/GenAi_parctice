'''33. write a program to calculate the monthly income of a person using the following 
commission schedule : (use if-else-if statement). 
Monthly sales income 
>= Rs.50,000 Rs.375 + 16% sales. 
>= Rs.50,000 but >=Rs.40,000 Rs. 350+14% sales. 
<= Rs.40,000 but >=Rs.30,000 Rs. 325+12% sales. 
<= Rs.30,000 but >=Rs.20,000 Rs. 300+9% sales. 
<= Rs.20,000 but >=Rs.10,000 Rs. 250+5% sales. 
<= Rs.10,000 Rs. 200+3% sales. '''

sales = float(input("Enter monthly sales income: "))    # 250000

if sales >= 50000:
    income = 375 + 0.16 * sales
elif sales >= 40000:
    income = 350 + 0.14 * sales
elif sales >= 30000:
    income = 325 + 0.12 * sales
elif sales >= 20000:
    income = 300 + 0.09 * sales
elif sales >= 10000:
    income = 250 + 0.05 * sales
else:
    income = 200 + 0.03 * sales

print("Monthly income =", income)

# output:
# Monthly income = 40375.0


# 35.write a program to read a 3 digit number and find whether the middle digit is 
# numerically equal to the sum of the other two digits and prints an appropriate response.

num = int(input("Enter a 3-digit number: "))    # 264
a = num // 100        # first digit
b = (num // 10) % 10  # middle digit
c = num % 10          # last digit

if b == a + c:
    print("Middle digit equals sum of other two.")
else:
    print("Condition not satisfied.")


# output:
# Middle digit equals sum of other two.




'''36.A Company insures its drivers in the following cases 
1. If the driver is married. 
2. If the driver is unmarried, male and above 30 years of age. 
3. If the driver is unmarried, female and above 25 years of age. 
In all other cases, the driver is not insured. If the marital status, sex, age of the 
driver are the inputs, write a program to determine whether the driver is insured 
or not. (use nested-if). '''

married = input("Married? (yes/no): ").lower()          # yes
sex = input("Sex? (male/female): ").lower()             # male
age = int(input("Enter age: "))                         # 35

if married == "yes":
    print("Driver is insured.")
else:
    if sex == "male":
        if age > 30:
            print("Driver is insured.")
        else:
            print("Driver is not insured.")
    elif sex == "female":
        if age > 25:
            print("Driver is insured.")
        else:
            print("Driver is not insured.")
    else:
        print("Invalid input for sex.")


# output:
# Driver is insured.