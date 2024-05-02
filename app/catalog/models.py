from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subordinates')

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'employee'
