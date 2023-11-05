## exercism.io leap challenge


def is_leap_year(year):
    """Leap years occur on every year that is evenly divisible by 4 except every year that is evenly divisible by 100 unless the year is also evenly divisible by 400"""

    if year % 4 == 0:
        return not year % 100 == 0 or year % 400 == 0

    return False
