import pandas as pd
# getting state income tax brackets and standard deductions for single and MFJ

# filing_status = 'MFJ'
# state_of_residence = 'CA'
# inflation_rate = 0.03
# base_year = 2025
# projection_year = 2025


def state_brax_standed(file, filing_stat, state, inf_rate, base_yr, proj_yr):
    state_brackets_df = pd.read_csv(file)
    state_brackets_single_df = state_brackets_df[['State', 'Single Brackets', 'Single Rates', 'Single Standard Deduction']]
    state_brackets_mfj_df = state_brackets_df[['State', 'MFJ Brackets', 'MFJ Rates', 'MFJ Standard Deduction']]

    if filing_stat == 'MFJ':
        state_tax_brackets_base = state_brackets_mfj_df[state_brackets_mfj_df['State'] == state]
    else:
        state_tax_brackets_base = state_brackets_single_df[state_brackets_single_df['State'] == state]

    state_tax_brackets_base_final = list(state_tax_brackets_base.itertuples(index=False, name=None))
    state_stan_deduct_base = float(state_tax_brackets_base.iloc[0, 3])
    state_stan_deduct = state_stan_deduct_base * (1 + inf_rate) ** (proj_yr - base_yr)
    return state_tax_brackets_base_final, state_stan_deduct




