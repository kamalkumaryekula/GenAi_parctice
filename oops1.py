class Student:
    student_feeses = []
    def __init__(self,name,age,fees):

        self.name = name
        self.age = age
        self.fees = fees
        self.student_feeses.append(self.fees)
    

    @classmethod
    def get_revenue(cls):
        rev = 0
        for i in cls.student_feeses:
            rev += i

        return rev
    
    @staticmethod
    def add(p,q):
        return p+q
    

s1 = Student("Rama",23,50000)
s2 = Student("sita",22,60000)

revenue = Student.get_revenue()
print(revenue)