def filter_inconsistent_rate_values_tst_30(input_rates):
    if len(input_rates) < 2:
        return input_rates
    filtered_rates = []
    for i in range(len(input_rates)):
        r = input_rates[i]
        if rate_is_inconsistent(r):
            # prendre le jour précédent ou suivant
            reference_rate = None
            if i > 0:
                reference_rate = input_rates[i-1]
            else:
                reference_rate = input_rates[i+1]
            patched_rate = r
            patched_rate["rate_open"] = reference_rate["rate_open"]
            patched_rate["rate_close"] = reference_rate["rate_close"]
            patched_rate["rate_high"] = reference_rate["rate_high"]
            patched_rate["rate_low"] = reference_rate["rate_low"]
            filtered_rates.append(patched_rate)
        else:
            filtered_rates.append(r)

    return filtered_rates