from django.utils import timezone
import random
from models import Employee

for i in range(50):
    full_name = f"Employee {i}"
    position = "Position"
    hire_date = timezone.now()
    salary = random.randint(20000, 100000)
    Employee.objects.create(full_name=full_name, position=position, hire_date=hire_date, salary=salary)


employees = Employee.objects.all()

for i, employee in enumerate(employees):
    if i > 0:
        manager_index = random.randint(0, 6)
        employee.manager = employees[manager_index]
        employee.save()
