from catalog.models import Employee
from django_seed import Seed

seeder = Seed.seeder()

seeder.add_entity(Employee, 1000, {
    'full_name': lambda x: seeder.faker.name(),
    'position': lambda x: seeder.faker.job(),
    'hire_date': lambda x: seeder.faker.date_this_century(),
    'salary': lambda x: seeder.faker.random_number(digits=5),
    'manager': lambda x: Employee.objects.order_by('?').first()
})

seeder.execute()
