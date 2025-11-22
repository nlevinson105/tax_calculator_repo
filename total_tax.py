# import libraries and modules
import pandas as pd
from tax_calculator_dir.fed_income_tax import fed_income_tax
from tax_calculator_dir.fed_capital_gains_tax import fed_ltcg_tax
from tax_calculator_dir.fed_payroll_tax import fed_payroll_tax
from state_income_tax import state_income_tax
from state_brax_standed import state_brax_standed
from fed_inc_brax_standed import fed_inc_brax_standed
from fed_ltcg_brax import fed_ltcg_brax
from fed_payroll_brax import fed_payroll_brax

# defining the ATL variables
filing_status = 'MFJ'
ages = [27, 27]
blind_status = ['n', 'n']
state_of_residence = 'CA'
emp_status = 'employee'
inflation_rate = 0.03
base_year = 2025
projection_year = 2025
ltcg_plus_qual_div_inc = 0
earned_inc = 200000
other_inc = 5000  # add more detail later
gross_inc = ltcg_plus_qual_div_inc + earned_inc + other_inc
student_loan_interest = 0
pre_tax_acct_conts = 0
other_atl_deducts = 0  # add more detail later
atl_deducts = student_loan_interest + pre_tax_acct_conts + other_atl_deducts
agi = gross_inc - atl_deducts
other_magi_add_backs = 0  # add more detail later
magi_add_backs = student_loan_interest + pre_tax_acct_conts + other_magi_add_backs
magi = agi + magi_add_backs

# getting state income tax brackets and standard deductions for single and MFJ
state_tax_brackets_base_final, state_stan_deduct = (
    state_brax_standed('state_tax_brackets.csv', filing_status, state_of_residence, inflation_rate,
                       base_year, projection_year))

# getting fed income tax brackets and standard deductions for single and MFJ
fed_inc_tax_brackets_base_final, fed_stan_deduct = (
    fed_inc_brax_standed('fed_inc_tax_brackets.csv', filing_status, ages, blind_status, magi,
                         inflation_rate, base_year, projection_year))

# getting fed LTCG brackets for single and MFJ
fed_ltcg_tax_brackets_base_final = fed_ltcg_brax('fed_ltcg_tax_brackets.csv', filing_status)

# getting fed payroll tax brackets for single and MFJ, employee and self-employed
fed_payroll_tax_brackets_base_final = fed_payroll_brax(filing_status, emp_status)

# defining the BTL variables
itemized_deducts = 0  # add more detail later
qbi_deduct = 0  # add more detail later
fed_taxable_inc = max(agi - max(fed_stan_deduct, itemized_deducts) - qbi_deduct, 0)
state_taxable_inc = max(agi - max(state_stan_deduct, itemized_deducts), 0)

refundable_tax_creds = 0  # add more detail later
non_refundable_tax_creds = 0  # add more detail later
total_tax_creds = refundable_tax_creds + non_refundable_tax_creds
amt_liab = 0  # add more detail later


def total_tax_calculator():
    total_tax = 0
    a = max(fed_income_tax(fed_taxable_inc, ltcg_plus_qual_div_inc, base_year, projection_year,
                           inflation_rate, fed_inc_tax_brackets_base_final), amt_liab)
    b = fed_ltcg_tax(fed_taxable_inc, ltcg_plus_qual_div_inc, base_year, projection_year,
                     inflation_rate, fed_ltcg_tax_brackets_base_final)
    c = fed_payroll_tax(earned_inc, base_year, projection_year,
                        inflation_rate, fed_payroll_tax_brackets_base_final)
    d = state_income_tax(state_taxable_inc, base_year, projection_year,
                         inflation_rate, state_tax_brackets_base_final)

    for i in [a, b, c, d]:
        total_tax += i

    tax_liab = max(total_tax - non_refundable_tax_creds, 0) - refundable_tax_creds
    eff_fed_tax_rate = ((a + b + c) / fed_taxable_inc) if fed_taxable_inc > 0 else 0
    eff_state_tax_rate = (d / state_taxable_inc) if state_taxable_inc > 0 else 0
    tax_liab_output = f'You owe ${tax_liab: .2f} of taxes for {projection_year}'
    eff_fed_inc_tax_rate_output =\
        f'Your effective federal income tax rate is {eff_fed_tax_rate * 100: .2f}% for {projection_year}'
    eff_state_inc_tax_rate_output =\
        f'Your effective state income tax rate is {eff_state_tax_rate * 100: .2f}% for {projection_year}'
    return tax_liab_output, eff_fed_inc_tax_rate_output, eff_state_inc_tax_rate_output


print(total_tax_calculator())

















































