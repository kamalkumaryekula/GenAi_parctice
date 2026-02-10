class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

        print(self.name)
        print(self.age)

    def info(self):
        print(self.name)
        return f"Hi {self.name} your age is {self.age}" 
    
obj = Student("Ram",23)
res = obj.info()
print(res)