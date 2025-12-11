# cleaning the data, removing special characters,space in name and salary.
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


# sort based on salaries.
emp_rec = [(1, 'Nick', 23, 45000.0),
            (2, 'Nick Jr.', 63, 245000.0),
            (3, 'Nick Sr.', 53, 145000.0),
            (4, 'Dan', 23, 45000.0),
            (5, 'Steve',23,46000.0)]


sorted_records = sorted(emp_rec, key=lambda x:x[3])
for rec in sorted_records:
    print(rec)




#descending order.
emp_rec = [(1, 'Nick', 23, 45000.0),
            (2, 'Nick Jr.', 63, 245000.0),
            (3, 'Nick Sr.', 53, 145000.0),
            (4, 'Dan', 23, 45000.0),
            (5, 'Steve',23,46000.0)]


sorted_records = sorted(emp_rec, key=lambda x:x[3], reverse = True)
for rec in sorted_records:
    print(rec)




#Find all the employee names who have the highest and lowest salaries.
emp_rec = [(1, 'Nick', 23, 45000.0),
            (2, 'Nick Jr.', 63, 245000.0),
            (3, 'Nick Sr.', 53, 145000.0),
            (4, 'Dan', 23, 45000.0),
            (5, 'Steve',23,46000.0)]



salaries = [rec[3] for rec in emp_rec]

min_salary = min(salaries)
max_salary = max(salaries)

lowest_paid = [rec[1] for rec in emp_rec if rec[3] == min_salary]
highest_paid = [rec[1] for rec in emp_rec if rec[3] == max_salary]

print("Lowest salary employees:", lowest_paid)
print("Highest salary employees:", highest_paid)    



# updated emp_details.
emp_rec = [
    (1, 'Nick', 23, 45000.0),
    (2, 'Nick Jr.', 63, 245000.0),
    (3, 'Nick Sr.', 53, 145000.0),
    (4, 'Dan', 23, 45000.0),
    (5, 'Steve', 23, 46000.0)
]

updated_emp_rec = []
for rec in emp_rec:
    tax_rate = 0.05 if (rec[3]*12) <= 500000 else (0.10 if (rec[3]*12) < 1000000 else 0.15)
    net_salary = rec[3] * (1 - tax_rate)
    updated_emp_rec.append((rec[0], rec[1], rec[2], net_salary))

print(updated_emp_rec)
