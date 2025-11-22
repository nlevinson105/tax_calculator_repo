# getting fed payroll tax brackets for single and MFJ, employee and self-employed

# filing_status = 'MFJ'
# emp_status = 'employee'


def fed_payroll_brax(filing_stat, emp_stat):
    payroll_tax_brackets_employee_mfj_base = [
        (176100, 0.0765),
        (250000, 0.0145),
        (float('inf'), 0.0235)
    ]

    payroll_tax_brackets_employee_single_base = [
        (176100, 0.0765),
        (200000, 0.0145),
        (float('inf'), 0.0235)
    ]

    payroll_tax_brackets_self_employed_mfj_base = [
        (176100, 0.153),
        (250000, 0.029),
        (float('inf'), 0.038)
    ]

    payroll_tax_brackets_self_employed_single_base = [
        (176100, 0.153),
        (200000, 0.029),
        (float('inf'), 0.038)
    ]

    if filing_stat == 'MFJ' and emp_stat == 'employee':
        bracket_df = payroll_tax_brackets_employee_mfj_base
    elif filing_stat == 'MFJ':
        bracket_df = payroll_tax_brackets_self_employed_mfj_base
    elif filing_stat == 'Single' and emp_stat == 'employee':
        bracket_df = payroll_tax_brackets_employee_single_base
    else:
        bracket_df = payroll_tax_brackets_self_employed_single_base

    fed_payroll_tax_brackets_base_final = bracket_df
    return fed_payroll_tax_brackets_base_final

