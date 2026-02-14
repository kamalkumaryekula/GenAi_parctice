

# multiple
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def hinfo(self):
        print(self.name,self.age)
    

class Employee(Human):
    def __init__(self,name,age,emp_id,salary):
        super().__init__(name,age)
        self.emp_id = emp_id
        self.salary = salary

    def einfo(self):
        super().hinfo()
        print(self.emp_id,self.salary)


class Manager(Employee):
    def __init__(self,name,age,emp_id,salary,department):
        super().__init__(name,age,emp_id,salary)
        self.department = department

    def minfo(self):
        super().einfo()
        print(self.department)


obj = Manager("Kamal",23,1234,150000,"Development")
obj.minfo()




# multiple inheritance
class Father:
    def __init__(self,name):
        self.name = name

    def info(self):
        print("we are in father class")

class Mother:
    def __init__(self,name):
        self.name = name

    def info(self):
        print("we are in mother class")


class Child(Father,Mother):
    def __init__(self,name):
        self.name = name
    
    def info(self):
        print("i am in my class")


obj = Child("rahul")
obj.info()



# 17.write a program to calculate the gross salary of kamal.
# if DA is 40% of his salary,and HRA is 20% of salary .

salary = float(input("Enter your monthly salary: "))    #100000
da = 0.4 * salary
hra = 0.2 * salary
gross_salary = salary + da + hra

print(f"Gross salary is {gross_salary}")

#output:
#Gross salary is 160000.0



# 18.The distance between two cities in Km. is input through the keyboard. 
# Write a program to convert and print the result in meters and centimeters. 

distance_km = float(input("Enter Distance between two cities: "))   #20
distance_m = distance_km * 1000
distance_cm = distance_m * 1000

print("Distance in meters : ",distance_m)
print("Distance in centi meters : ",distance_cm)

#output:
#Distance in meters :  20000.0
#Distance in centi meters :  2000000

#19.write a program to convert currency from dollars to rupees.

dollars = float(input("Enter dollars: "))   #50
rupees =  dollars * 90.57

print(f"currency in {rupees} rupees for {dollars} dollars")

#output:
#currency in 4528.5 rupees for 50.0 dollars

#20.print your address by taking input from user.

address = input("Enter your address: ")     #GUNTUR
print("Your address is:", address)

#output:
#Your address is: GUNTUR


# 21.Write a program to print the area of a triangle if b and h values are given. 

b = float(input("Enter base: "))    #10
h = float(input("Enter height: "))  #15
area = 0.5 * b * h

print("Area of triangle =", area)

#output:
#Area of triangle = 75.0


#22. Area of triangle using Heron's formula.

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

s = (a + b + c) / 2   # semi-perimeter
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # square root using **0.5

print(f"Area of triangle is {area:.2f}")

#output:
#Area of triangle = 808.67