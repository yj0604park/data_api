from django.contrib import admin

from . import models


@admin.register(models.Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "gross_pay",
        "net_pay",
        "total_deduction",
        "total_adjustment",
        "total_withheld",
    )
    list_filter = ("date",)


@admin.register(models.SalaryDetailItem)
class SalaryDetailItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(models.SalaryDetail)
class PayDetailAdmin(admin.ModelAdmin):
    list_display = (
        "salary",
        "salary_detail",
        "amount",
        "detail_type",
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("salary", "salary_detail")
