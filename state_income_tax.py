# import pandas as pd
# inflation_rate = 0.03
# base_year = 2025
# projection_year = 2025
# gross_inc = 121080
# atl_deducts = 10000
# adj_gross_inc = gross_inc - atl_deducts
#
# state_brackets_df = pd.read_csv('state_tax_brackets.csv')
# state_brackets_single_df = state_brackets_df[['State', 'Single Brackets',
#                                               'Single Rates', 'Single Standard Deduction']]
# state_brackets_mfj_df = state_brackets_df[['State', 'MFJ Brackets', 'MFJ Rates', 'MFJ Standard Deduction']]
# residence_state = 'NY'
# tax_filing_status = 'MFJ'
#
# if tax_filing_status == 'MFJ':
#     bracket_df = state_brackets_mfj_df[state_brackets_mfj_df['State'] == residence_state]
# else:
#     bracket_df = state_brackets_single_df[state_brackets_single_df['State'] == residence_state]
#
# state_stan_deduct = bracket_df.iloc[0, 3]
# state_bracket_final = list(bracket_df.itertuples(index=False, name=None))
#
# itemized_deducts = 0
# taxable_inc = adj_gross_inc - max(state_stan_deduct, itemized_deducts)

# tax_brackets_mfj_base = [
#     (base_year, 21512, 0.01),
#     (base_year, 50998, 0.02),
#     (base_year, 80490, 0.04),
#     (base_year, 111732, 0.06),
#     (base_year, 141732, 0.08),
#     (base_year, 721318, 0.093),
#     (base_year, 865574, 0.103),
#     (base_year, 1000000, 0.113),
#     (base_year, 1442628, 0.123),
#     (base_year, float('inf'), 0.133)  # float('inf') means positive infinity
# ]


def state_income_tax(income, base_year, proj_year, inflation_rate, brackets):
    tax = 0
    previous_bracket_limit = 0

    tax_brackets_mfj = [(x, y * (1 + inflation_rate) ** (proj_year - base_year), z,
                         s * (1 + inflation_rate) ** (proj_year - base_year))
                        for x, y, z, s in brackets]

    for state, bracket_limit, rate, stan_ded in tax_brackets_mfj:
        if income > bracket_limit:
            tax += (bracket_limit - previous_bracket_limit) * rate
        else:
            tax += (income - previous_bracket_limit) * rate
            break
        previous_bracket_limit = bracket_limit

    return max(tax, 0)


# print(state_bracket_final)
# print(state_stan_deduct)
# print(state_income_tax(taxable_inc, base_year, projection_year, inflation_rate, state_bracket_final))





