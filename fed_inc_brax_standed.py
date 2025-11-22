import pandas as pd
from tax_phaseout import phaseout
# getting fed income tax brackets and standard deductions for single and MFJ


def fed_standard_deduction(age, blind, mod_adj_gross_inc, filing_stat):
    fed_stan_deduct_base = 31500 if filing_stat == 'MFJ' else 15750
    over_65_stan_ded = 1600 if filing_stat == 'MFJ' else 2000
    blind_stan_ded = 1600 if filing_stat == 'MFJ' else 2000
    over_65_low_inc_stan_ded = 6000
    over_65_low_inc_stan_ded_phaseout = [150000, 250000] if filing_stat == 'MFJ' else [75000, 175000]

    fed_st_ded = fed_stan_deduct_base

    if len(age) == 2 and mod_adj_gross_inc <= over_65_low_inc_stan_ded_phaseout[1]:
        if age[0] >= 65 and age[1] >= 65:
            fed_st_ded += (over_65_stan_ded * 2 +
                           phaseout(mod_adj_gross_inc,
                                    over_65_low_inc_stan_ded_phaseout[0],
                                    over_65_low_inc_stan_ded_phaseout[1],
                                    over_65_low_inc_stan_ded) * 2)
        elif age[0] < 65 and age[1] < 65:
            pass
        else:
            fed_st_ded += (over_65_stan_ded +
                           phaseout(mod_adj_gross_inc,
                                    over_65_low_inc_stan_ded_phaseout[0],
                                    over_65_low_inc_stan_ded_phaseout[1],
                                    over_65_low_inc_stan_ded))
    elif len(age) == 2:
        if age[0] >= 65 and age[1] >= 65:
            fed_st_ded += (over_65_stan_ded * 2)
        elif age[0] < 65 and age[1] < 65:
            pass
        else:
            fed_st_ded += over_65_stan_ded
    elif mod_adj_gross_inc <= over_65_low_inc_stan_ded_phaseout[1]:
        if age[0] >= 65:
            fed_st_ded += (over_65_stan_ded +
                           phaseout(mod_adj_gross_inc,
                                    over_65_low_inc_stan_ded_phaseout[0],
                                    over_65_low_inc_stan_ded_phaseout[1],
                                    over_65_low_inc_stan_ded))
        else:
            pass
    else:
        if age[0] >= 65:
            fed_st_ded += over_65_stan_ded
        else:
            pass

    if len(blind) == 2:
        if blind[0] == 'y' and blind[1] == 'y':
            fed_st_ded += (blind_stan_ded * 2)
        elif blind[0] == 'n' and blind[1] == 'n':
            pass
        else:
            fed_st_ded += blind_stan_ded
    else:
        if blind[0] == 'y':
            fed_st_ded += blind_stan_ded
        else:
            pass

    return fed_st_ded


def fed_inc_brax_standed(file, filing_stat, age, blind, magi, inf, base_yr, proj_yr):
    fed_inc_brackets_df = pd.read_csv(file)
    fed_inc_brackets_single_df = fed_inc_brackets_df[['Tax Rate', 'Single Brackets']]
    fed_inc_brackets_mfj_df = fed_inc_brackets_df[['Tax Rate', 'MFJ Brackets']]

    if filing_stat == 'MFJ':
        bracket_df = fed_inc_brackets_mfj_df
    else:
        bracket_df = fed_inc_brackets_single_df

    fed_inc_tax_brackets_base_final = list(bracket_df.itertuples(index=False, name=None))

    fed_stan_ded = fed_standard_deduction(age, blind, magi, filing_stat)
    fed_stan_deduct = fed_stan_ded * (1 + inf) ** (proj_yr - base_yr)
    return fed_inc_tax_brackets_base_final, fed_stan_deduct


