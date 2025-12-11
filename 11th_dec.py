##1. Employee Records
#🔧 Task: Sort Employees by Salary
employees = [
    (101, "Ravi", 55000),
    (102, "Anita", 72000),
    (103, "Kiran", 48000),
    (104, "Meena", 65000)
]

#1. Ascending Order (Lowest to Highest)
sorted_employees = sorted(employees, key=lambda x: x[2])
print(sorted_employees)


#2. Descending Order (Highest to Lowest)
sorted_employees_desc = sorted(employees, key=lambda x: x[2], reverse=True)
print(sorted_employees_desc)


#3. Sort by Salary, then by Name (Tie-breaker)
sorted_employees_multi = sorted(employees, key=lambda x: (x[2], x[1]))
print(sorted_employees_multi)


'''🌍 Real-world Use Cases
Payroll systems: Generate salary slips in order of pay.

HR dashboards: Show top earners or lowest earners.

Recruitment apps: Filter candidates by expected salary.

Data analysis: Compare salary distribution across departments.'''


#🔧 Task: Filter Employees Above Threshold
employees = [
    (101, "Ravi", 55000),
    (102, "Anita", 72000),
    (103, "Kiran", 48000),
    (104, "Meena", 65000)
]

#1. Basic Filtering
threshold = 60000
filtered = [emp for emp in employees if emp[2] > threshold]
print(filtered)


#2. Dynamic Threshold (User Input)
threshold = int(input("Enter salary threshold: "))
filtered = [emp for emp in employees if emp[2] > threshold]

print(f"Employees earning above ₹{threshold}:")
for emp in filtered:
    print(f"ID: {emp[0]}, Name: {emp[1]}, Salary: ₹{emp[2]}")


#3. Combine with Sorting
threshold = 50000
filtered_sorted = sorted(
    [emp for emp in employees if emp[2] > threshold],
    key=lambda x: x[2],
    reverse=True
)
print(filtered_sorted)



'''🌍 Real-world Use Cases
Payroll systems: Identify employees eligible for bonus (e.g., salaries above ₹60,000).

HR dashboards: Filter high earners for reporting.

Recruitment apps: Compare expected salaries with company budget.

Data analysis: Study salary distribution above certain levels.'''


#🔧 Task: Update Salary for a Specific Employee
employees = [
    (101, "Ravi", 55000),
    (102, "Anita", 72000),
    (103, "Kiran", 48000),
    (104, "Meena", 65000)
]

#1. Simple Update by ID
emp_id_to_update = 103
new_salary = 52000

updated_employees = [
    (emp[0], emp[1], new_salary) if emp[0] == emp_id_to_update else emp
    for emp in employees
]

print(updated_employees)


#2. Update by Name
name_to_update = "Meena"
new_salary = 70000

updated_employees = [
    (emp[0], emp[1], new_salary) if emp[1] == name_to_update else emp
    for emp in employees
]

print(updated_employees)


#3. Interactive Update (User Input)
emp_id = int(input("Enter Employee ID to update: "))
new_salary = int(input("Enter new salary: "))

employees = [
    (emp[0], emp[1], new_salary) if emp[0] == emp_id else emp
    for emp in employees
]

print("Updated employee list:", employees)



'''🌍 Real-world Use Cases
Payroll systems: Adjust salaries after appraisals.

HR dashboards: Update employee records when promotions happen.

Recruitment apps: Modify expected salary during negotiations.

Data analysis: Simulate salary changes for forecasting.'''


##2. Student Grades
students = [
    ("Ravi", "Math", 85),
    ("Anita", "Math", 92),
    ("Kiran", "Science", 78),
    ("Meena", "Science", 88),
    ("Ravi", "English", 75),
    ("Anita", "English", 82),
    ("Kiran", "English", 90)
]

#🔧 Task: Find Highest Scorer in Each Subject
#1. Using a Dictionary
highest = {}

for name, subject, marks in students:
    if subject not in highest or marks > highest[subject][1]:
        highest[subject] = (name, marks)

print(highest)


#2. Formatted Report
for subject, (name, marks) in highest.items():
    print(f"Highest in {subject}: {name} with {marks} marks")


#3. Using groupby (from itertools)
from itertools import groupby

students_sorted = sorted(students, key=lambda x: x[1])  # sort by subject
for subject, group in groupby(students_sorted, key=lambda x: x[1]):
    top = max(group, key=lambda x: x[2])
    print(f"Highest in {subject}: {top[0]} with {top[2]} marks")



'''🌍 Real-world Use Cases
School dashboards: Show top scorer per subject.

Exam analysis: Identify subject toppers for awards.

Recruitment tests: Find best candidates in each skill area.

Data visualization: Plot subject toppers on charts.'''


#🔧 Task: Calculate Average Marks per Student
students = [
    ("Ravi", "Math", 85),
    ("Anita", "Math", 92),
    ("Kiran", "Science", 78),
    ("Meena", "Science", 88),
    ("Ravi", "English", 75),
    ("Anita", "English", 82),
    ("Kiran", "English", 90)
]
#1. Using a Dictionary

averages = {}

for name, subject, marks in students:
    if name not in averages:
        averages[name] = []
    averages[name].append(marks)

for name, marks_list in averages.items():
    avg = sum(marks_list) / len(marks_list)
    print(f"{name}: {avg:.2f}")


#2. Using defaultdict for Cleaner Code
from collections import defaultdict

marks_dict = defaultdict(list)

for name, subject, marks in students:
    marks_dict[name].append(marks)

for name, marks_list in marks_dict.items():
    avg = sum(marks_list) / len(marks_list)
    print(f"{name}: {avg:.2f}")


#3. Using Pandas (for larger datasets)
import pandas as pd

df = pd.DataFrame(students, columns=["Name", "Subject", "Marks"])
print(df.groupby("Name")["Marks"].mean())



'''🌍 Real-world Use Cases
School dashboards: Show average marks per student across subjects.

Exam analysis: Identify overall toppers.

Recruitment tests: Calculate candidate averages across skill tests.

Data visualization: Plot average marks per student in charts.'''


#🔧 Task: Group Students by Subject
students = [
    ("Ravi", "Math", 85),
    ("Anita", "Math", 92),
    ("Kiran", "Science", 78),
    ("Meena", "Science", 88),
    ("Ravi", "English", 75),
    ("Anita", "English", 82),
    ("Kiran", "English", 90)
]
#1. Using a Dictionary
groups = {}

for name, subject, marks in students:
    if subject not in groups:
        groups[subject] = []
    groups[subject].append((name, marks))

print(groups)


#2. Formatted Report
for subject, records in groups.items():
    print(f"{subject}:")
    for name, marks in records:
        print(f"  {name} → {marks}")


#3. Using defaultdict (Cleaner Code)
from collections import defaultdict

groups = defaultdict(list)

for name, subject, marks in students:
    groups[subject].append((name, marks))

for subject, records in groups.items():
    print(subject, ":", records)


#4. Using Pandas (for larger datasets)
import pandas as pd

df = pd.DataFrame(students, columns=["Name", "Subject", "Marks"])
print(df.groupby("Subject")["Name"].apply(list))



'''🌍 Real-world Use Cases
School dashboards: Show all students grouped by subject.

Exam analysis: Compare performance subject-wise.

Recruitment tests: Group candidates by skill area.

Data visualization: Plot subject-wise student distributions'''



##3. Orders
orders = [
    ("Order1", [("Apple", 2, 50), ("Banana", 5, 10)]),
    ("Order2", [("Milk", 1, 40), ("Bread", 2, 30), ("Eggs", 12, 5)]),
    ("Order3", [("Rice", 1, 500), ("Dal", 2, 120)])
]

#🔧 Task: Calculate Total Bill
#1. Basic Calculation
for order_id, items in orders:
    total = sum(qty * price for _, qty, price in items)
    print(f"{order_id} → Total Bill = ₹{total}")


#2. Store Results in a Dictionary
bills = {order_id: sum(qty * price for _, qty, price in items) for order_id, items in orders}
print(bills)


#3. Formatted Report
for order_id, items in orders:
    print(f"\n{order_id}:")
    total = 0
    for name, qty, price in items:
        subtotal = qty * price
        total += subtotal
        print(f"  {name} ({qty} × ₹{price}) = ₹{subtotal}")
    print(f"Total Bill = ₹{total}")


'''🌍 Real-world Use Cases
Retail billing systems: Calculate total bill per customer order.

Restaurant apps: Compute bill per table.

E-commerce carts: Show total cost before checkout.

Analytics: Compare average order values.'''



