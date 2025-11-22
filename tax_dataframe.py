import pandas as pd

filing_status = 'MFJ'
inflation_rate = 0.03
base_year = 2025

tax_brackets_mfj_base = [
    (base_year, 23850, 0.1),
    (base_year, 96950, 0.12),
    (base_year, 206700, 0.22),
    (base_year, 394600, 0.24),
    (base_year, 501050, 0.32),
    (base_year, 751600, 0.35),
    (base_year, float('inf'), 0.37)  # float('inf') means positive infinity
]


years = list(range(2026, 2030))
column_names = ['year', 'threshold', 'rate']
projected_brackets_df = pd.DataFrame(tax_brackets_mfj_base, columns=column_names)

for yr in years:
    next_bracket = [(x + (yr - base_year), y * (1+inflation_rate) ** (yr - base_year), z)
                    for x, y, z in tax_brackets_mfj_base]
    next_bracket_df = pd.DataFrame(next_bracket, columns=column_names)
    projected_brackets_df = pd.concat([projected_brackets_df, next_bracket_df], axis=0)
print(projected_brackets_df)
print('done')

