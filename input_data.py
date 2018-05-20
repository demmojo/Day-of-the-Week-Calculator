
# Get input and test ranges of allowable input


def user_input():
    day = input('Please input the number of the day: ')
    while True:
        if day:  # checks for input
            if day.isdigit():  # checks input is a number
                if 1 <= int(day) <= 31:  # checks input is in range
                    break
                else:
                    day = (input('Please input a number between 1-31: '))
        else:
            day = input('Please input the number of the day: ')
    month = input('Please input the number of the month: ')

    while True:
        if month:
            if month.isdigit():
                if int(month) <= int(month) <= 12:
                    break
                else:
                    month = (input('Please input a correct month number 1-12: '))
        else:
            month = input('Please input a month: ')

    year = input('Please input a year after 1582 AD: ')

    while True:
        if year:
            if year.isdigit():
                if 1582 <= int(year):
                    break
                else:
                    year = input('Please input a year after 1582 AD: ')
        else:
            year = input('Please input a year: ')

    return day, month, year
