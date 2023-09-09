import unittest
from collections import defaultdict

#TC O(n * k * log(k)) / EC: O(n * k)
def group_anagram(arr):
    if not arr:
        return [[""]]

    groups = {}
    for i in range(len(arr)):
        word,word_sorted = arr[i], ''.join(sorted(arr[i]))
        if word_sorted in groups:
            groups[word_sorted] += [word]
        else:
            groups[word_sorted] = [word]
    values = [x for x in groups.values()]
    return values

def group_anagram_clean(arr):
    if not arr:
        return [[]]

    groups = defaultdict(list)

    for word in arr:
        sorted_word = ''.join(sorted(word))
        groups[sorted_word].append(word)

    return list(groups.values())

# Time complexity: O(n * k) | Space Complexity: O(n)
def group_anagram_optmized(arr):
    anagram_groups = defaultdict(list)
    for word in arr:
        # Calculates a hash based on the letters of the word
        char_count = [0] * 26  # Suppose there are only lowercase letters
        for char in word:
            char_count[ord(char) - ord('a')] += 1
        # convert hash in tuple to be used as keys
        char_tuple = tuple(char_count)
        anagram_groups[char_tuple].append(word)
    return list(anagram_groups.values())

class Test(unittest.TestCase):
    test_cases = [
        (["eat","tea","tan","ate","nat","bat"],[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
        ([""], [[""]]),
        (["a"], [['a']]),
    ]
    functions = [group_anagram, group_anagram_clean, group_anagram_optmized]
    def test_group_anagram(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()