import unittest

# Seven different symbols represent Roman numerals with the following values:
# Symbol	Value
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000

# Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

#     If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
#     If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
#     Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.

# Given an integer, convert it to a Roman numeral.

#TC O(1)
#TS O(1)
def IntToRoman(s):
    symbols = [
        ["I",1],
        ["IV",4],
        ["V",5],
        ["IX",9],
        ["X",10],
        ["XL",40],
        ["L",50],
        ["XC",90],
        ["C",100],
        ["CD",400],
        ["D",500],
        ["CM",900],
        ["M",1000]
    ]
    result = ""
    for sym, val in symbols[::-1]:
        calc = s // val
        if calc < 1: continue
        result += sym * calc
        s = s % val
    return result

class Test(unittest.TestCase):
    test_cases = [
        (3749, "MMMDCCXLIX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (400, "CD")
    ]
    functions = [IntToRoman]
    def test_int_to_roman(self):
        for function in self.functions:
            for s, expected in self.test_cases:
                result = function(s)
                assert result == expected

if __name__ == '__main__':
    unittest.main()