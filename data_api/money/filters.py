import django_filters

from .models import Salary
from .models import SalaryDetailItem


class SalaryFilter(django_filters.FilterSet):
    class Meta:
        model = Salary
        fields = {"date": ["exact", "gte", "lte"]}


class SalaryDetailFilter(django_filters.FilterSet):
    class Meta:
        model = SalaryDetailItem
        fields = {
            "name": ["exact", "icontains"],
        }
