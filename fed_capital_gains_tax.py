import pandas as pd

# filing_status = 'MFJ'
# inflation_rate = 0.03
# base_year = 2025
# ltcg_plus_qual_divs = 156700
# other_income = 0
# gross_inc = ltcg_plus_qual_divs + other_income
# atl_deducts = 0
# adj_gross_inc = gross_inc - atl_deducts
# stan_deduct = 30000 if filing_status == 'MFJ' else 15000
# itemized_deducts = 0
# taxable_inc = adj_gross_inc - max(stan_deduct, itemized_deducts)

# fed_ltcg_brackets_df = pd.read_csv('fed_ltcg_tax_brackets.csv')
# fed_ltcg_brackets_single_df = fed_ltcg_brackets_df[['Rate', 'Single Brackets']]
# fed_ltcg_brackets_mfj_df = fed_ltcg_brackets_df[['Rate', 'MFJ Brackets']]
# tax_filing_status = 'MFJ'
#
# if tax_filing_status == 'MFJ':
#     bracket_df = fed_ltcg_brackets_mfj_df
# else:
#     bracket_df = fed_ltcg_brackets_single_df
# fed_ltcg_bracket_final = list(bracket_df.itertuples(index=False, name=None))
#
# ltcg_tax_brackets_mfj_base = [
#     (base_year, 96700, 0),
#     (base_year, 600050, 0.15),
#     (base_year, float('inf'), 0.2)
# ]


def fed_ltcg_tax(total_taxable_income, total_ltcg_income, base_year, proj_year, inflation_rate, brackets):
    income = total_taxable_income - total_ltcg_income
    ltcg_tax = 0
    previous_bracket_limit = 0

    tax_brackets_mfj = [(x, y * (1 + inflation_rate) ** (proj_year - base_year))
                        for x, y in brackets]

    for rate, bracket_limit in tax_brackets_mfj:
        if income > bracket_limit:
            ltcg_tax += 0
        elif total_taxable_income > bracket_limit:
            ltcg_tax += (bracket_limit - income) * rate
        else:
            ltcg_tax += (total_taxable_income - previous_bracket_limit) * rate
            break
        previous_bracket_limit = max(bracket_limit, income)

    return max(ltcg_tax, 0)


# print(fed_ltcg_bracket_final)




