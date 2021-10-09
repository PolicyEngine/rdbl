from math import log10, floor


def _round_sf(num, sf=2):
    return round(num, sf - int(log10(abs(num))) - 1)


def _highest_matching(mapping, key):
    if key in mapping:
        return key, mapping[key]
    keys = list(mapping.keys())
    if key < min(keys):
        matching_key = min(keys)
    else:
        matching_key = keys[sorted(keys + [key]).index(key) - 1]
    return matching_key, mapping[matching_key]


def _readable(
    num, sf=3, prefixes={0: ""}, suffixes={0: ""}
):
    try:
        float(num)
    except:
        raise Exception("Passed a non-numerical input.")
    num_rounded = _round_sf(num, sf=sf)
    if num < 0:
        return "-" + _readable(-num, sf=sf, prefixes=prefixes, suffixes=suffixes)
    if num == 0:
        return prefixes[0] + "0" + suffixes[0]
    place_value = int(log10(num_rounded))
    _, prefix = _highest_matching(prefixes, place_value)
    place, suffix = _highest_matching(suffixes, place_value)
    reduced_num = _round_sf(num / (10 ** place), sf)
    if place >= max(suffixes.keys()):
        num_str = format(int(reduced_num), ",")
    else:
        num_str = str(reduced_num).rstrip("0").rstrip(".")
    return prefix + num_str + suffix


def _financial(num, currency_code, **kwargs):
    prefixes = {"GBP": "£", "EUR": "€", "USD": "$"}
    if currency_code not in prefixes:
        raise Exception("Unsupported currency.")
    small_units = {"GBP": "p", "EUR": "c", "USD": "c"}
    if num >= 1 and num < 10:
        return prefixes[currency_code] + str(round(num, 2))
    if num >= 0.01 and num < 1:
        return str(int(round(num * 1e+2))) + small_units[currency_code]
    if num > 0 and num < 1e-2:
        return prefixes[currency_code] + "~0"
    if num == 0:
        return prefixes[currency_code] + "0"
    if num < 0:
        return "-" + _financial(-num, currency_code)
    prefixes = {
        0: prefixes[currency_code]
    }
    suffixes = {
        0: "",
        3: "k",
        6: "m",
        9: "bn",
        12: "tr",
    }
    return _readable(num, prefixes=prefixes, suffixes=suffixes, **kwargs)


def gbp(num, **kwargs):
    return _financial(num, currency_code="GBP", **kwargs)


def eur(num, **kwargs):
    return _financial(num, currency_code="EUR", **kwargs)


def usd(num, **kwargs):
    return _financial(num, currency_code="USD", **kwargs)


def num(number):
    if number == 0:
        return number
    suffixes = {
        0: "",
        3: "k",
        6: "m",
        9: "bn",
        12: "tr",
    }
    return _readable(number, suffixes=suffixes)
