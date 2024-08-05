import unittest

# You are given a string letters made of N English letters. 
# Count the number of different letters that appear in both uppercase and lowercase where all lowercase occurrences of the given letter appear before any uppercase occurrence. For example, for letters = "aaAbcCABBc" the answer is 2. The condition is met for letters 'a' and b', but not for 'c.
#TC (n)
#SC O(1)
def count_valid_letters(letters):
    first_occurrence = set()
    valid_letters = set()
    seen_upper = set()

    for i, letter in enumerate(letters):
        if letter.islower():
            if letter.upper() in seen_upper:
                valid_letters.discard(letter)
                continue
            first_occurrence.add(letter)
        elif letter.isupper() and letter.lower() in first_occurrence:
            seen_upper.add(letter)
            lower_letter = letter.lower()
            valid_letters.add(lower_letter)

    return len(valid_letters)

class Test(unittest.TestCase):
    test_cases = [
        ("aaAbcCABBc",2),
    ]
    functions = [count_valid_letters]
    def test_count_valid_letters(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                assert expected == function(arr)

if __name__ == '__main__':
    unittest.main()