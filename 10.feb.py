

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

