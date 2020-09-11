from math import log

def readable(num, sf=1, base=10, currency=False, small_unit="p", prefix="", suffixes={0: ""}):
    try:
        float(num)
    except:
        raise Exception("Passed a non-numerical input.")
    if num < 0:
        return "-" + readable(-num, sf, base, currency, small_unit, prefix, suffixes)
    places = list(suffixes.keys())
    if num != 0:
        num_digits = max(int(log(num, base)), min(places))
    else:
        num_digits = max(1, min(places))
    if num_digits in places:
        place = num_digits
    else:
        place = max(0, places[sorted(places + [num_digits]).index(num_digits) - 1])
    if currency and num_digits < 1:
        sf = num_digits + 2
    rounded = str(round(num / (base ** (place - sf))) / (base ** sf))
    suffix = suffixes[place]
    if currency and num_digits < 1 and "." in rounded:
        ending = rounded.split(".")[-1]
        rounded = rounded.split(".")[0] + "." + ending[:2] + "".join(["0"] * (2 - len(ending[:2])))
        if float(rounded) < 0.01:
            prefix = "£"
            rounded = "~0"
        elif float(rounded) < 1:
            suffix = small_unit
            rounded = rounded.split(".")[-1]
    else:
        rounded = rounded.rstrip("0").rstrip(".")
    return prefix + rounded + suffix

def financial(num, currency_code):
    prefixes = {
        "GBP": "£",
        "EUR": "€",
        "USD": "$"
    }
    if currency_code not in prefixes:
        raise Exception("Unsupported currency.")
    prefix = prefixes[currency_code] if (abs(num) >= 1 or num == 0) else ""
    small_units = {
        "GBP": "p",
        "EUR": "c",
        "USD": "c"
    }
    small_unit = small_units[currency_code]
    suffixes = {
        0: "",
        3: "k",
        6: "m",
        9: "bn",
        12: "tr",
    }
    return readable(num, currency=True, small_unit=small_unit, prefix=prefix, suffixes=suffixes)

def gbp(num):
    return financial(num, currency_code="GBP")

def eur(num):
    return financial(num, currency_code="EUR")

def usd(num):
    return financial(num, currency_code="USD")

def bytes_SI(num):
    suffixes = {
        0: "B",
        3: "kB",
        6: "MB",
        9: "GB",
        12: "TB",
        15: "PB"
    }
    return readable(num, base=10, suffixes=suffixes)

def bytes_bin(num):
    suffixes = {
        0: "B",
        10: "KiB",
        20: "MiB",
        30: "GiB",
        40: "TiB"
    }
    return readable(num, base=2, suffixes=suffixes)

def num(number):
    suffixes = {
        0: "",
        3: "k",
        6: "m",
        9: "bn",
        12: "tr",
    }
    return readable(number, suffixes=suffixes)