import datetime
import unittest
# Given a date, return the corresponding day of the week for that date.

# The input is given as three integers representing the day, month and year respectively.

# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
# time complexity :  O(1)
def day_of_the_week(day, month, year):
    return datetime.datetime(year=year, day=day, month=month).strftime("%A")

# def day_of_the_week_ii(day, month, year):
#     return datetime (year=year, day=day, month=month).strftime("%A")

class Test(unittest.TestCase):
    test_cases = [
        (31,  8, 2019, "Saturday"),
        (18,7, 1999, "Sunday"),
    ]
    functions = [day_of_the_week]
    def test_day_of_the_week(self):
        for function in self.functions:
            for day, month, year, expected in self.test_cases:
                result = function(day, month, year)
                assert result == expected

if __name__ == '__main__':
    unittest.main()