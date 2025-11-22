import pandas as pd
# filing_status = 'MFJ'
# inflation_rate = 0.03
# base_year = 2025
# gross_inc = 144000
# atl_deducts = 14000
# adj_gross_inc = gross_inc - atl_deducts
# stan_deduct = 30000 if filing_status == 'MFJ' else 15000
# itemized_deducts = 0
# taxable_inc = adj_gross_inc - max(stan_deduct, itemized_deducts)

# fed_inc_brackets_df = pd.read_csv('fed_inc_tax_brackets.csv')
# fed_inc_brackets_single_df = fed_inc_brackets_df[['Tax Rate', 'Single Brackets']]
# fed_inc_brackets_mfj_df = fed_inc_brackets_df[['Tax Rate', 'MFJ Brackets']]
# tax_filing_status = 'MFJ'
#
# if tax_filing_status == 'single':
#     bracket_df = fed_inc_brackets_mfj_df
# else:
#     bracket_df = fed_inc_brackets_single_df
# fed_inc_bracket_final = list(bracket_df.itertuples(index=False, name=None))

# tax_brackets_mfj_base = [
#     (base_year, 23850, 0.1),
#     (base_year, 96950, 0.12),
#     (base_year, 206700, 0.22),
#     (base_year, 394600, 0.24),
#     (base_year, 501050, 0.32),
#     (base_year, 751600, 0.35),
#     (base_year, float('inf'), 0.37)
# ]
# float('inf') means positive infinity


def fed_income_tax(total_taxable_income, total_ltcg_income, base_year, proj_year, inflation_rate, brackets):
    income = total_taxable_income - total_ltcg_income
    tax = 0
    previous_bracket_limit = 0

    tax_brackets_mfj = [(x, y * (1 + inflation_rate) ** (proj_year - base_year))
                        for x, y in brackets]

    for rate, bracket_limit in tax_brackets_mfj:
        if income > bracket_limit:
            tax += (bracket_limit - previous_bracket_limit) * rate
        else:
            tax += (income - previous_bracket_limit) * rate
            break
        previous_bracket_limit = bracket_limit

    return max(tax, 0)


# print(fed_inc_bracket_final)



















