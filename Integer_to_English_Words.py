import unittest
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# time complexity :  O(n)
def numberToWords(num):
    if num == 0:
        return "Zero"
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    suffixes = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion", "Sextillion", "Septillion", "Octillion", "Nonillion", "Decillion"]
    words = []
    i = 0
    while num > 0:
        triplet = num % 1000
        num = num // 1000
        if triplet == 0:
            i += 1
            continue
        temp = []
        if triplet // 100 > 0:
            temp.append(ones[triplet // 100])
            temp.append("Hundred")
        if triplet % 100 >= 10 and triplet % 100 <= 19:
            temp.append(teens[triplet % 10])
        else:
            if triplet % 100 >= 20:
                temp.append(tens[triplet % 100 // 10])
            if triplet % 10 > 0:
                temp.append(ones[triplet % 10])
        if i > 0:
            temp.append(suffixes[i])
        words = temp + words
        i += 1
    return " ".join(words)


def numberToWords_ii(num: int) -> str:
    ## RC ##
    ## APPROACH : BRUTE FORCE ##
    ## Main intent of the interviewer when asked this question is , he is testing how you are handling the test cases and how elagantly you are using sub problems to get to the final solution ## (so focus on edge cases)
    ## 1. For a two digit number if there is no ones digit 20 -> twenty + " " (number generally), dont leave the space behind, use if else case with "" (empty). Similarly for 20,000 etc.
        
    one_digit = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }

    two_digit = {
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen'
    }
        
    tens = {
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty',
        5: 'Fifty',
        6: 'Sixty',
        7: 'Seventy',
        8: 'Eighty',
        9: 'Ninety'
    }

    def get_three_digit_num(num):
        if( not num ) : return ""
        if( not num// 100 ): return get_two_digit_num(num)
        return one_digit[ num // 100 ] + " Hundred" + ((" " + get_two_digit_num( num % 100 )) if( num % 100 ) else "")

    def get_two_digit_num( num ):
        if not num:
            return ''
        elif num < 10:
            return one_digit[ num ]
        elif num < 20:
            return two_digit[ num ]
                # edge case 1
        return tens[ num//10 ] + ((" " + one_digit[ num % 10 ]) if( num % 10 ) else "")
    
    # edge case
    if(num == 0): return "Zero"
    
    billion = num // 1000000000
    million = (num - billion * 1000000000) // 1000000
    thousand = (num - billion * 1000000000 - million * 1000000) // 1000
    last_three = num - billion * 1000000000 - million * 1000000 - thousand * 1000
    
    result = ''
    if billion:        
        result = get_three_digit_num(billion) + ' Billion'
    if million:
        # space only when prev result is not None
        result += ' ' if result else ''    
        result += get_three_digit_num(million) + ' Million'
    if thousand:
        result += ' ' if result else ''
        result += get_three_digit_num(thousand) + ' Thousand'
    if last_three:
        result += ' ' if result else ''
        result += get_three_digit_num(last_three)
    return result

def numberToWords_iii(num):
    dict = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }
        
    result = ""
        
    if num == 0:
        return "Zero"

    def convert(n):
        if n == 0:
            return ""
        if n in dict:
            return dict[n]
        if n // 1000000000 > 0:
            return (convert(n // 1000000000) + " Billion " + convert(n%1000000000)).strip()
        if n // 1000000 > 0:
            return (convert(n // 1000000) + " Million " + convert(n%1000000)).strip()
        if n // 1000 > 0:
            return (convert(n // 1000) + " Thousand " + convert(n%1000)).strip()
            
        if n // 100 > 0:
            return (convert(n // 100) + " Hundred " + convert(n%100)).strip()
        if n // 10 > 0:
            return (convert((n // 10)*10) + " " + convert(n%10)).strip()
        
        return ""

        return convert(num).strip()
class Test(unittest.TestCase):
    test_cases = [
        (123, "One Hundred Twenty Three"),
        (12345, "Twelve Thousand Three Hundred Forty Five"),
        (1234567, "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
    ]
    functions = [numberToWords, numberToWords_ii, numberToWords_iii]
    def test_numberToWords(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()