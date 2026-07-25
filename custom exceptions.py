class SalaryError(Exception):
    pass

def get_salary(salary):
    if salary<0:
        raise SalaryError("salary cannot be negative")
    else:
        bonus=0.1*salary
        return bonus+salary

salary=int(input("enter your salary:"))
final_salary=get_salary(salary)
print(final_salary)