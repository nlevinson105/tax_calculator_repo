# filing_status = 'MFJ'
# emp_status = 'employee'
# inflation_rate = 0.03
# base_year = 2025
# earned_inc = 300000
#
# payroll_tax_brackets_employee_mfj_base = [
#     (176100, 0.0765),
#     (250000, 0.0145),
#     (float('inf'), 0.0235)
# ]
#
# payroll_tax_brackets_employee_single_base = [
#     (176100, 0.0765),
#     (200000, 0.0145),
#     (float('inf'), 0.0235)
# ]
#
# payroll_tax_brackets_self_employed_mfj_base = [
#     (176100, 0.153),
#     (250000, 0.029),
#     (float('inf'), 0.038)
# ]
#
# payroll_tax_brackets_self_employed_single_base = [
#     (176100, 0.153),
#     (200000, 0.029),
#     (float('inf'), 0.038)
# ]
#
# if filing_status == 'MFJ' and emp_status == 'employee':
#     bracket_df = payroll_tax_brackets_employee_mfj_base
# elif filing_status == 'MFJ':
#     bracket_df = payroll_tax_brackets_self_employed_mfj_base
# elif filing_status == 'Single' and emp_status == 'employee':
#     bracket_df = payroll_tax_brackets_employee_single_base
# else:
#     bracket_df = payroll_tax_brackets_self_employed_single_base
#
# fed_payroll_tax_brackets_base_final = bracket_df


def fed_payroll_tax(income, base_year, proj_year, inflation_rate, brackets):
    tax = 0
    previous_bracket_limit = 0

    tax_brackets_mfj = [(x * (1 + inflation_rate) ** (proj_year - base_year), y)
                        for x, y in brackets]

    for bracket_limit, rate in tax_brackets_mfj:
        if income > bracket_limit:
            tax += (bracket_limit - previous_bracket_limit) * rate
        else:
            tax += (income - previous_bracket_limit) * rate
            break
        previous_bracket_limit = bracket_limit

    return max(tax, 0)


# print(fed_payroll_tax_brackets_base_final)













