from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    manager = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = (
            'full_name',
            'position',
            'hire_date',
            'salary',
            'manager'
        )
