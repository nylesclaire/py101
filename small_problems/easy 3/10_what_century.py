def ordinal_suffix(number):
    str_num = str(number)
    if len(str_num) >= 2 and str_num[-2] == "1":
        return "th"
    match str_num[-1]:
        case "1":
            return "st"
        case "2":
            return "nd"
        case "3":
            return "rd"
        case _:
            return "th"

def century(year):
    if year <= 100:
        return "1st"
    str_yr = str(year)
    if str_yr.endswith("00"):
        cent = str_yr[:-2]
    else:
        cent = str(int(str_yr[:-2]) + 1)
    return cent + ordinal_suffix(cent)

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True