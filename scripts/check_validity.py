from data_api.money.models import Salary, SalaryDetailItem, SalaryDetail


def run():
    print("Checking pay details")
    for salary in Salary.objects.all():
        print("Checking salary: ", salary.date)
        salary.check_detail()

    print("Checking salary details")
    detail_items = SalaryDetailItem.objects.all()
    lower_case = {}

    for item in detail_items:
        lower_case_name = item.name.lower()
        if lower_case_name in lower_case:
            print("Duplicate name: ", item.name)
            lower_case[lower_case_name].append(item)
        else:
            lower_case[lower_case_name] = [item]

    for name, items in lower_case.items():
        if len(items) > 1:
            print("Duplicate name: ", name)
            normalized_name = SalaryDetailItem.get_nomalized_name(name)
            print("Normalized name: ", normalized_name)

            surviving_item = items[0]
            surviving_item.name = normalized_name
            surviving_item.save()

            for item in items[1:]:
                for detail in item.salarydetail_set.all():
                    detail.salary_detail = surviving_item
                    detail.save()

                item.delete()
        else:
            print("Unique name: ", name)
            normalized_name = SalaryDetailItem.get_nomalized_name(name)

            if items[0].name != normalized_name:
                items[0].name = normalized_name
                items[0].save()
