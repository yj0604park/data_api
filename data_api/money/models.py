from django.db import models
from collections import defaultdict


class Salary(models.Model):
    date = models.DateField()
    gross_pay = models.DecimalField(max_digits=10, decimal_places=2)
    total_adjustment = models.DecimalField(max_digits=10, decimal_places=2)
    total_withheld = models.DecimalField(max_digits=10, decimal_places=2)
    total_deduction = models.DecimalField(max_digits=10, decimal_places=2)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date}: {self.gross_pay}: {self.net_pay}"

    def check_detail(self):
        total_sum = 0
        detail_sum = defaultdict(int)

        for salary_detail in self.salarydetail_set.all():
            total_sum += salary_detail.amount
            detail_sum[salary_detail.detail_type] += salary_detail.amount

        assert total_sum == self.net_pay
        assert detail_sum[SalaryDetailType.PAY] == self.gross_pay
        assert detail_sum[SalaryDetailType.ADJUSTMENT] == self.total_adjustment
        assert detail_sum[SalaryDetailType.WITHHELD] == self.total_withheld
        assert detail_sum[SalaryDetailType.DEDUCTION] == self.total_deduction


class SalaryDetailItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @classmethod
    def get_nomalized_name(cls, name):
        return name.title()


class SalaryDetailType(models.TextChoices):
    PAY = "PAY", "PAY"
    ADJUSTMENT = "ADJ", "ADJUSTMENT"
    WITHHELD = "WIT", "WITHHELD"
    DEDUCTION = "DED", "DEDUCTION"


class SalaryDetail(models.Model):
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    salary_detail = models.ForeignKey(SalaryDetailItem, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    detail_type = models.TextField(max_length=3, choices=SalaryDetailType.choices)

    def __str__(self):
        return f"{self.salary.id}: {self.salary_detail.id}: {self.detail_type}: {self.amount}"
