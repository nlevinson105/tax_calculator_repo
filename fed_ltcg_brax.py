import pandas as pd
# getting fed LTCG brackets for single and MFJ

# filing_status = 'MFJ'


def fed_ltcg_brax(file, filing_stat):
    fed_ltcg_brackets_df = pd.read_csv(file)  # add code for NIIT thresholds
    fed_ltcg_brackets_single_df = fed_ltcg_brackets_df[['Rate', 'Single Brackets']]
    fed_ltcg_brackets_mfj_df = fed_ltcg_brackets_df[['Rate', 'MFJ Brackets']]

    if filing_stat == 'MFJ':
        bracket_df = fed_ltcg_brackets_mfj_df
    else:
        bracket_df = fed_ltcg_brackets_single_df

    fed_ltcg_tax_brackets_base_final = list(bracket_df.itertuples(index=False, name=None))
    return fed_ltcg_tax_brackets_base_final




