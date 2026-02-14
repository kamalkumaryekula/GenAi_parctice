
'''
#6.write a program to find out the area and circumference of a circle.

radius = float(input("Enter the radius of the circle: "))    # 20
area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius

print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")

#output:
# Area of the circle: 1256.00
# Circumference of the circle: 125.60


#7.write a program to find out the surface area and volume of a sphere.

radius = float(input("Enter the radius of the sphere: "))    # 5
surface_area = 4 * 3.14 * radius * radius
volume = (4/3) * 3.14 * radius * radius * radius

print(f"Surface area of the sphere: {surface_area:.2f}")
print(f"Volume of the sphere: {volume:.2f}")

#output:
# Surface area of the sphere: 314.00
# Volume of the sphere: 523.33

#8.write a program to find out the volume of a cylinder.

radius = float(input("Enter the radius of the cylinder: "))   # 5
height = float(input("Enter the height of the cylinder: "))   # 7
volume = 3.14 * radius * radius * height

print(f"Volume of the cylinder: {volume:.2f}")

#output:
# Volume of the cylinder: 549.50

#9.write a program to convert age in years to age in days.

age_years = float(input("Enter your age in years: "))   # 24
age_days = age_years * 365

print(f"Your age in days: {age_days:.0f}")

#output:
#Your age in days: 8760

#10.write a program to calculate simple interest and compound interest.

principal = float(input("Enter the principal amount: "))            # 100000
rate = float(input("Enter the rate of interest (% per annum): "))   # 12
time = float(input("Enter the time period (in years): "))           # 5

simple_interest = (principal * rate * time) / 100
amount_simple = principal + simple_interest

compound_interest = principal * (1 + rate / 100) ** time
compound_interest_amount = compound_interest - principal

print(f"Simple Interest: {simple_interest:.2f}")
print(f"Amount after Simple Interest: {amount_simple:.2f}")
print(f"Compound Interest: {compound_interest_amount:.2f}")
print(f"Amount after Compound Interest: {compound_interest:.2f}")

#output:
# Simple Interest: 60000.00
# Amount after Simple Interest: 160000.00
# Compound Interest: 76234.17
# Amount after Compound Interest: 176234.17   '''



# 11.write a program to calculate the total mechanical energy of a particle.  e = mgh + 1/2mv^2  

mass = float(input("Enter the mass of the particle (kg): "))  #25
gravity = 9.8
height = float(input("Enter the height (h): "))               #10
velocity = float(input("Enter the velocity (v): "))           #20

mechanical_energy = (mass * gravity * height) + (0.5 * mass * velocity**2)

print(f"Total Mechanical Energy: {mechanical_energy:.2f}")

#output:
# Total Mechanical Energy: 7450.00


#12. Convert Seconds → Hours, Minutes, Seconds

total_seconds = int(input("Enter the total seconds: "))    #5650

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"Hours: {hours}")           
print(f"Minutes: {minutes}")       
print(f"Seconds: {seconds}")       

#output:
# Hours: 1
# Minutes: 34
# Seconds: 10    


#13. A milkman mixes 4 litres of milk with 1 litre of water and sells the mixture at Rs. 4.15 per litre,
# but he buys milk at Rs. 3.25 per litre. Find the profit.

milk_rate = 3.25
sell_rate = 4.15

milk_qty = float(input("Enter milk quantity (litres): "))

# For every 4 litres milk, 1 litre water added
water_qty = milk_qty / 4
total_qty = milk_qty + water_qty

cost_price = milk_qty * milk_rate
selling_price = total_qty * sell_rate
gain = selling_price - cost_price

print("Gain =", gain)

#output:
# Gain = 3.875


# 14. convert temperature from celsius to fahrenheit.

celsius = float(input("Enter the temperature in Celsius: "))   #100
fahrenheit = (celsius * 9/5) + 32

print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")

#output:
# Temperature in Fahrenheit: 212.00   

# 15.swaping two two variables without having temporary variable.

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

a = a + b
b = a - b
a = a - b

print(f"a: {a}")
print(f"b: {b}")

#output:
# a: 20
# b: 10    

# 16. write a program to find the distance between two points in a cartesian plane.

x1 = float(input("Enter x1: "))   #2
y1 = float(input("Enter y1: "))   #5
x2 = float(input("Enter x2: "))   #3
y2 = float(input("Enter y2: "))   #6

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f"Distance between points: {distance:.2f}")

#output:
# Distance between points: 1.41




