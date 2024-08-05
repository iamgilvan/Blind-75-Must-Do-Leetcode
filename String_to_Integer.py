
import unittest
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

#     Whitespace: Ignore any leading whitespace (" ").
#     Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
#     Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
#     Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

# Return the integer as the final result.

# time complexity :  O(n)
def string_to_integer(s):
    s = s.strip()  # Remove any leading or trailing whitespace
    if not s:
        return 0
    # Handle the optional '+' or '-' sign
    sign = 1
    start_index = 0
    max_int = 2147483647
    min_int = -2147483648
    if s[0] == '-':
        sign = -1
        start_index = 1
    elif s[0] == '+':
        start_index = 1
    # Parse the digits
    num = 0
    for i in range(start_index, len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
            # Check for overflow and clamp to limits
            if sign == 1 and num > max_int:
                return max_int
            if sign == -1 and -num < min_int:
                return min_int
        else:
            break
    return sign * num

class Test(unittest.TestCase):
    test_cases = [
        ("42", 42),
        (" -042", -42),
        ("1337c0d3", 1337),
        ("0-1", 0),
        ("words and 987", 0),
    ]
    functions = [string_to_integer]
    def test_string_to_integer(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()