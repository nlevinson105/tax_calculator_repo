# filing_status = 'Single'
# age = 30
# magi = 161500
# lower_bound = 236000 if filing_status == 'MFJ' else 150000
# upper_bound = 246000 if filing_status == 'MFJ' else 165000
# roth_ira_cont_limit_2025 = 7000 if age < 50 else 8000
#
# print(roth_ira_cont_limit_2025)


def phaseout(income, lower, upper, value):
    allowed_value = 0
    if income > upper:
        pass
    elif income < lower:
        allowed_value = value
    else:
        allowed_value = (1 - ((income - lower) / (upper - lower))) * value
    return allowed_value


# print(phaseout(magi, lower_bound, upper_bound, roth_ira_cont_limit_2025))

