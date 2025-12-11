
# Write a program to add and subtract two numbers.
a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
addition = a + b
subtraction = a - b
print("addition of a and b is:",addition)
print("subtraction of a and b is:",subtraction)



#write a program to multiply and divide two numbers in the form of (4*3 = 12 , 8/4 = 2)
a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
multiplication = a * b
division = a / b
print(f'{a} * {b} = {multiplication}')
print(f'{a} / {b} = {division}')


#square and cube of a given number
number = int(input("Enter value of number:"))
square = number**2
cube = number**3
print(f'square value:{square}') 
print(f'cube value:{cube}')  


#find the square root of a given number using sqrt().
##we need to import sqrt from the math library,by then we can access sqrt()

import math
num = int(input("enter a number:"))
print(math.sqrt(num))   


#area and perimeter of a square.
s = int(input("side of a square:"))
perimeter = 4*s
area = s**2
print(f'perimeter of the square is : {perimeter}')
print(f'area of the square is : {area}')   


#area and circumference of a circle.
r = int(input("Enter value of radius:"))
circumference = 2*3.14*r
area = 3.14*(r**2)
print(f'circumference of the circle: {round(circumference,2)}')   #use round()  to limit decimal values
print(f'area of the circle: {area}')   


#area of the sphere.
import math
r = int(input("enter the value of radius:"))
area_of_sphere = 4*math.pi*(r**2)
print(f'area of the sphere is: {round(area_of_sphere ,2)}')   



# write a program to find the volume of the cylinder.
## formula for volume of cylinder is pi*(r**2)*h
import math
r = int(input("enter value of radius:"))
h = int(input("enter value of height:"))
volume_of_cylinder = math.pi*(r**2)*h
print(f'volume of the cylinder : {round(volume_of_cylinder,2)}')   



#find age in days.
#find simple intrest and compond intrest.
p = int(input(" enter principle amount:"))
t = int(input("enter no of years:"))    # time in years
n = int(input("enter no of times compounded:"))  # how many intrest is compounded per year
r = int(input("enter rate in percentage:"))
simple_intrest = (p*t*r)/100
a = p*((1 + (r/(n*100)))**(n*t))
compound_intrest = a - p
print(f'simple intrest: {simple_intrest}')
print(f'compound intrest: {round(compound_intrest , 2)}')   



#mechanical energy.
m = int(input("mass of the object: "))
g = 9.8
h = int(input("enter height:"))
v = float(input("enter velocity:"))
energy = ((m*g*h) + ((m*(v**2))/2))
print(f'mechanical energy is: {energy}')    



## Program to convert seconds into hours, minutes, and seconds
total_seconds = int(input("Enter time in seconds: "))
hours = total_seconds // 3600   
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{total_seconds} seconds = {hours} hours, {minutes} minutes, {seconds} seconds")


# distance between two points.
x1 = int(input("enter value of x1 :"))
x2 = int(input("enter value of x2 :"))
y1 = int(input("enter value of y1 :"))
y2 = int(input("enter value of y2 :"))
distance = (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
print(f'distance between two points: {round(distance ,2)}')    



#Write a program to print the area of a triangle if three sides are given. 
a = int(input('Enter value of a :'))
b = int(input('Enter value of b :'))
c = int(input('Enter value of c :'))
s = (a + b + c)/2
area_of_triangle  =( s*(s-a)*(s-b)*(s-c))**0.5
print(f'Area of a triangle whose side are {a} , {b} , {c} is {round(area_of_triangle,3)}')   



#Write a program to print the area of a triangle if b and h values are given. 
b = int(input("enter value of base :"))
h = int(input("enter value of height :"))
area_of_the_triangle = (b*h)/2
print(f'area of triangle whose base {b} and height{h} is {area_of_the_triangle}')   


#write a program to print adress
h_no = input("enter house number:")
street_name = input("enter street name:")
village_name = input("enter village name")
mandal_name = input("enter mandal name:")
state = input("enter state name:")
pincode = input("enter pincode")
print(f'H.no:{h_no}\nStreet_name:{street_name}\nvillage_name:{village_name}\nmandal_name:{mandal_name}\nstate:{state}\npincode:{pincode}')



#gross salary 
salary = int(input("Enter salary: "))
hra = 0.2*salary
da = 0.4*salary
gross_salary = salary + hra + da
print("hra:",hra)
print("da:",da)
print("gross salary:",gross_salary) 


#exchange usd into inr.
usd = int(input("enter how many dollars you have:"))
exchange_rate = 89.58
inr = usd * exchange_rate
print(f'amount in rupees after converting from usd:',inr)   



# interchanging two locations.
a = input("enter location of a:")
b = input("enter location of b:")
a , b = b , a
print("location of a:",a)
print("location of b:",b)     



#fehrinheit to celcius.
f = float(input("enter temperature in fehrinheit: "))
c = (f - 32)*(5 / 9)
print("temperature in celcius is:",round(c ,2))   



#age in days.
from datetime import date

year = int(input("enter birth year:"))
month = int(input("enter birth month:"))
day = int(input("enter birth day:"))
date_of_birth = date(year, month, day)

today = date.today()

age_in_days = (today -(date_of_birth)).days
print("age in days:",age_in_days)   



#gain of milk vendor.
cost_price = float(input("enter cost price:"))
selling_price = float(input("entar selling price:"))
gain_of_profit = ((selling_price*5) - (cost_price*4))
print("gain of profit: ",gain_of_profit)   






