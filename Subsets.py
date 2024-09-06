import unittest

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

#TC  O(n * 2^n)
#SC O(1)
# def get_sub_set(numbers):
#     ps = {frozenset()}
#     for element in numbers:
#         additions = set()
#         for subset in ps:
#             partial = subset.union(str(element))
#             additions.add(partial)
#         ps = ps.union(additions)

#     print([list(x) for x in ps])
#     return ps

#TC  O(n * 2^n)
#SC O(1)
def get_sub_set(nums):
    res = []

    subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return

        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)

        # decision Not to include nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res

class Test(unittest.TestCase):
    s = [1,2,3]
    def test_power_set(self):
        ps = get_sub_set(self.s)
        self.assertEqual(len(ps), 8)

if __name__ == "__main__":
    unittest.main()