# t1 = (1231,"kamal",23,75000)
# t2 = (1232,"kumar",24,85000)
# t3 = (1233,"vamsi",22,95000)
# l = [t1,t2,t3]
# print(l)
# employees = l
# for _id,name,age,salary in employees:
#     print(_id,name,age,salary)



# 2

# n = int(input("enter no of employee details: "))
# employee_details = []
# for i in range(n):
#     _id = int(input("enter _id: "))
#     name = input("enter name: ")
#     age = int(input("enter age: "))
#     salary = int(input("Enter salary: "))

#     employee = (_id,name,age,salary)
#     employee_details.append(employee)
   
# print(employee_details)




# 2

# n= int(input("Enter no of Employees: "))
# loe = []
# for i in range(n):
#     _id,name,age,salary = input().split(",")
#     loe.append([_id,name,age,salary])
# loe_final = [(int(i[0]),i[1],int(i[2]),float(i[3])) for i in loe]
# print(f"list of Employees: {loe_final}")




# 3

# emp_rec = [(1, 'Nick', 23, 45000.0),
#             (2, 'Nick Jr.', 63, 245000.0),
#             (3, 'Nick Sr.', 53, 145000.0),
#             (4, 'Dan', 23, 45000.0),
#             (5, 'Steve',23,46000.0)]

# sorted_records = sorted(emp_rec, key=lambda x:x[3],reverse = True)
# for rec in sorted_records:
#     print(rec)





## maximum salary.

# emp_rec = [(1, 'Nick', 23, 45000.0),
#             (2, 'Nick Jr.', 63, 245000.0),
#             (3, 'Nick Sr.', 53, 145000.0),
#             (4, 'Dan', 23, 45000.0),
#             (5, 'Steve',23,46000.0)]

# max_sal = max(emp_rec, key=lambda x:x[3])
# for rec in max_sal:
#     print(rec,end = ",")



# # minimum salary.

# emp_rec = [(1, 'Nick', 23, 45000.0),
#             (2, 'Nick Jr.', 63, 245000.0),
#             (3, 'Nick Sr.', 53, 145000.0),
#             (4, 'Dan', 23, 45000.0),
#             (5, 'Steve',23,46000.0)]

# min_sal = min(emp_rec, key=lambda x:x[3])
# for rec in min_sal:
#     print(rec,end = ",")



# # employees with same min salary.

# emp_rec = [(1, 'Nick', 23, 45000.0),
#             (2, 'Nick Jr.', 63, 245000.0),
#             (3, 'Nick Sr.', 53, 145000.0),
#             (4, 'Dan', 23, 45000.0),
#             (5, 'Steve',23,46000.0)]
# min_sals = min(emp_rec,key = lambda x:x[-1])[-1]

# for rec in emp_rec:
#     if rec[-1]== min_sals:
#         print(rec)

    

#  


import re

emp_recs = [
    (1, 'Nick $$#  Jr.', 23, '45000.0$'), 
    (2, 'Nick Jr.', 63, '245000.0&&'),
    (3, 'Nick Sr.', 53, 145000.0), 
    (4, 'Dan  ^^', 23, '45000.0'), 
    (5, 'Steve', 23, 46000.0)
]

cleaned_recs = [
    (
        emp_id,
        ' '.join(re.sub(r'[^a-zA-Z0-9 .]', '', name).split()),   
        age,
        float(re.sub(r'[^0-9.]', '', str(salary)))               
    )
    for emp_id, name, age, salary in emp_recs
]

print(cleaned_recs)
