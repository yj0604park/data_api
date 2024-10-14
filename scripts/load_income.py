import json

from django.db import transaction
from typing import Dict

from data_api.money.models import (
    Salary,
    SalaryDetailItem,
    SalaryDetailType,
    SalaryDetail,
)


detail_type_to_key = {
    SalaryDetailType.PAY: "payDetail",
    SalaryDetailType.ADJUSTMENT: "adjustmentDetail",
    SalaryDetailType.WITHHELD: "taxDetail",
    SalaryDetailType.DEDUCTION: "deductionDetail",
}


def run():
    # open file
    with open("custom_data/income.json", "r") as f:
        # read file
        data = json.load(f)

        sid = transaction.savepoint()

        try:
            for node in data["data"]["salaryRelay"]["edges"]:
                salary = get_or_create_salary(node)

                for detail_type, _ in SalaryDetailType.choices:
                    create_salary_detail(
                        salary=salary,
                        detail=node["node"][detail_type_to_key[detail_type]],
                        detail_type=detail_type,
                    )

        except Exception as e:
            print("Error: ", e)
            transaction.savepoint_rollback(sid)


def get_or_create_salary(node):
    print("Processing node: ", node["node"]["id"])

    existing_salary = Salary.objects.filter(date=node["node"]["date"])
    if existing_salary.exists():
        print("Salary already exists")
        return existing_salary.first()

    # create a new object
    salary = Salary(
        date=node["node"]["date"],
        gross_pay=node["node"]["grossPay"],
        net_pay=node["node"]["netPay"],
        total_deduction=node["node"]["totalDeduction"],
        total_adjustment=node["node"]["totalAdjustment"],
        total_withheld=node["node"]["totalWithheld"],
    )

    # save the object
    salary.save()
    return salary


def create_salary_detail(salary: Salary, detail: Dict[str, str], detail_type: str):
    for key, value in detail.items():
        print(key, " ", value)
        detail = SalaryDetailItem.objects.get_or_create(name=key)
        print("Detail: ", detail)
        SalaryDetail.objects.get_or_create(
            salary=salary,
            salary_detail=detail[0],
            amount=value,
            detail_type=detail_type,
        )
