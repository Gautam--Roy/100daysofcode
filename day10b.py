def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """Return the number of days based on the input {year} and {month}"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 30, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month - 1]


year = int(input("Enter year: "))
month = int(input("Enter month: "))
days = days_in_month(year, month)
print(days)
