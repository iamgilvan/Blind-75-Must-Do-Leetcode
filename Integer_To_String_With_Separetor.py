import collections
import unittest

# Write a method IntToString which converts an integer to a string with thousands separators.
#TC O(d)
def int_to_string_with_thousands_separator(number):
    # Handle negative numbers
    is_negative = number < 0
    number = abs(number)
    # Convert number to string and reverse it for easier processing
    num_str = str(number)[::-1]

    # Initialize an empty result string
    result = []

    # Process every 3 digits and add a comma
    for i in range(0, len(num_str), 3):
        if i > 0:
            result.append(',')
        result.append(num_str[i:i+3])

    # Reverse the result list and join it to form the final string
    formatted_str = ''.join(result)[::-1]

    # Add the negative sign back if the number was negative
    if is_negative:
        formatted_str = '-' + formatted_str

    return formatted_str

class Test(unittest.TestCase):
    test_cases = [
        (1234567890, "1,234,567,890"),
        (-987654321, "-987,654,321"),
        (1000, "1,000"),
        (0, "0"),
    ]
    functions = [int_to_string_with_thousands_separator]
    def test_largest_coherent_group(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()