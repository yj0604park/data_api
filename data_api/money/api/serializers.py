from rest_framework import serializers

from data_api.money.models import Salary, SalaryDetailItem


class SalaryDetailSerializer(serializers.ModelSerializer[SalaryDetailItem]):
    class Meta:
        model = SalaryDetailItem
        fields = ["name"]


class SalarySerializer(serializers.ModelSerializer[Salary]):
    class Meta:
        model = Salary
        fields = [
            "id",
            "date",
            "gross_pay",
            "total_adjustment",
            "total_withheld",
            "total_deduction",
            "net_pay",
        ]
