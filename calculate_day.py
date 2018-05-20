from data_dict import century_dict, year_dict, month_dict

# Check website given in README.md for explanation about formula and values below


def calculate_day(day, month, year):
    # Transform year to known year number code
    year_code = str(year)[-2:]
    century_code = str(year)[:2]
    while True:
        if int(year_code) <= 27:
            year_final = int(year_dict[year_code])
            break
        elif 27 < int(year_code) <= 55:
            year_code = str(int(year_code) - 28)
            year_final = int(year_dict[year_code])
            break
        elif 55 < int(year_code) <= 83:
            year_code = str(int(year_code) - 56)
            year_final = int(year_dict[year_code])
            break
        elif 83 < int(year_code) <= 99:
            year_code = str(int(year_code) - 84)
            year_final = int(year_dict[year_code])
            break
    # Account for Leap years
    if int(year_code) % 4 == 0:
        if int(month) <= 2:
            month_final = int(month_dict[month]) - 1
        else:
            month_final = int(month_dict[month])
    else:
        month_final = int(month_dict[month])
    # Find day of week
    day_calc = (month_final + year_final + int(day) + int(century_dict[century_code])) % 7

    return day_calc
