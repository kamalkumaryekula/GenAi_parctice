
emp_records = \
[(1, 'Nick $$#  Jr.', 23, '45000.0$'),
(2, 'Nick Jr.', 63, '245000.0&**&'),
(3, 'Nick Sr.', 53, 145000.0),
(4, 'Dan  ^^', 23, '45000.0'),
(5, 'Steve', 23, 46000.0), 
(6, 'Steve Jr.', 24, '*****146000.0'), 
(7, '&&^^Steve    Sr.', 65, 446000.0)]

# 1. Sum of salaries of all the employees
#  2. Names of employees whose age < 25
#  3. Assume a tax slab of
#     a.  5% for salary <= 5 Lakhs/month; 
#     b. 10% if the salary is between 5 and 10 Lakhs/Month; 
#     c. 15 % for salary>= 10 Lakhs/Month;
#     update the net takeaway after deducting the tax in a new column and print the new data.
#     eg: [(_id, Name, Age, Salary, Salary_after_tax_deduction)]



# cleanead records.
print('1.--------------------------------------------------------------------------')
cleaned_emp_records = []
for rec in emp_records:
    _id, name, age, salary = rec

    name = ''.join(ch for ch in name if 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122 or ch == ' ')
    name = ' '.join(name.split())
    salary = float(''.join(ch for ch in str(salary) if ch.isdigit() or ch == '.'))
    cleaned_emp_records.append((_id, name, age, salary))

print(cleaned_emp_records)


# employees above 25 years.
print('2.--------------------------------------------------------------------------')
print([rec[1] for rec in cleaned_emp_records if rec[2] < 25])


# sum of salaries of all employees.
print('3.--------------------------------------------------------------------------')
total_salary = sum(salary for _id, name, age, salary in cleaned_emp_records)
print(sum([rec[3] for rec in cleaned_emp_records]))
print(total_salary)


# update records with tax deduction.
print('4.--------------------------------------------------------------------------')
#  3. Assume a tax slab of
#     a.  5% for salary <= 5 Lakhs/month; 
#     b. 10% if the salary is between 5 and 10 Lakhs/Month; 
#     c. 15 % for salary>= 10 Lakhs/Month;
#     update the net takeaway after deducting the tax in a new column and print the new data.
#     eg: [(_id, Name, Age, Salary, Salary_after_tax_deduction)]
updated_emp_records = []
#rec[3] = salary
for rec in cleaned_emp_records:
    if rec[3] <= 500000:
        tax_rate = 0.05
    elif 500000 < rec[3] < 1000000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15
    salary_after_tax = rec[3] * (1 - tax_rate)
    updated_emp_records.append((rec[0], rec[1], rec[2], rec[3], salary_after_tax))
print(updated_emp_records)




stu_records = \
[('_id', 'Name', 'Age', 'Marks'), 
(1, 'Steven', 23, (95, 90, 60, 65, 77, 80)),
(2, 'Nick', 24, (95, 93, 60, 65, 60, 81)),
(3, 'Peter', 23, (77, 90, 34, 76, 77, 80)),
(4, 'Dan', 23, (95, 58, 60, 65, 66, 89)),
(5, 'Tim', 25, (23, 55, 56, 43, 56, 45)), 
(6, 'Dave', 24, (0, 35, 55, 76, 77, 80)), 
(7, 'John', 27, (92, 'Ab', 60, 65, 77, 80)), 
(8, 'Jacob', 27, (98, 89, 60, 65, 77, 80)), 
(9, 'Chris', 25, (97, 98, 96, 99, 97, 89))]


# Rules:
# * If a person is absent for one exam/got 0 in any one subject/got < 35 in any one subject he is considered as failed.

# Queries:
# 1. Toppers Names.
# 2. Names of last grade students in the class (ignore failures).
# 3. Failures Names.
# 4. Sum of all their totals in ['Name', total] format ignore failures' data.
# 5. consider the subjects as (Machine Learning, AI, Python, CloudServices, Database, Prompt Engineering), Now
#     a. Get all the top and least marked names in AI (ignore failures).
#     b. Get the subject(s) with most toppers.
#     c. Get the subject(s) with most failures.

# cleaned student records.--------------------------------------------------------------------------')
cleaned_stu_records = []
for rec in stu_records[1:]:
    _id, name, age, marks = rec
    cleaned_marks = []
    for mark in marks:
        # try:
        #     cleaned_marks.append(int(mark))
        # except:
        #     cleaned_marks.append(0)
        if mark =="Ab" or mark == 0:
            cleaned_marks.append(0)
        else:
            cleaned_marks.append(int(mark))
    cleaned_stu_records.append((_id, name, age, tuple(cleaned_marks)))
print(cleaned_stu_records)


# 1.topper names
print('1.---------------------------------------')
topper = []
total = [sum(rec[3]) for rec in cleaned_stu_records]
max_total = max(total)
for rec in cleaned_stu_records:
    if sum(rec[3]) == max_total:
        topper.append(rec[1])
        print(topper)
