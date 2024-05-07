from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    manager = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = [
            'id',
            'full_name',
            'position',
            'hire_date',
            'salary',
            'manager'
        ]
        datatables_always_serialize = ('id',)

    def get_manager(self, obj):
        manager = Employee.objects.get(id=obj.id).manager_id
        if manager is None:
            return 'Boss'
        else:
            return Employee.objects.get(id=manager).full_name
