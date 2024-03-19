from employee import Employee
from db import conn

employees = [
    Employee(name='Tsotne', surname='Sharvadze', age=25),
    Employee(name='Mariam', surname='Kipshidze', age=24),
    Employee(name='Tinatin', surname='Tsakadze', age=20),
    Employee(name='Cillian', surname='Murphy', age=47),
    Employee(name='Tinatin', surname='Machabeli', age=36)
]

for employee in employees:
    employee.save()

conn.commit()


employees_tinatin = Employee.get_list(name='Tinatin')
print(employees_tinatin)
print(employees_tinatin[0].age > employees_tinatin[1].age)

employees_age_24 = Employee.get_list(age=24)
print(employees_age_24)
if employees_age_24:
    employees_age_24[0].delete()
    conn.commit()
else:
    print("No employees with age 24 found.")
