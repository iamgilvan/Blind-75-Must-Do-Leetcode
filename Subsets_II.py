import unittest

# Given an integer array nums that may contain duplicates, return all possible
# subsets
# (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

#TC  O(n * 2^n)
#SC O(1)
def get_sub_set_ii(nums):
    res = []
    nums.sort()
    def dfs(i, subset):
        if i == len(nums):
            res.append(subset.copy())
            return

        # all subsets that include nums[i]
        subset.append(nums[i])
        dfs(i + 1, subset)
        subset.pop()

        # all subsets that don't include nums[i]
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        dfs(i + 1, subset)

    dfs(0, [])
    return res


class Test(unittest.TestCase):
    s = [1,2,2]
    def test_subset_ii(self):
        ps = get_sub_set_ii(self.s)
        self.assertEqual(len(ps), 6)

if __name__ == "__main__":
    unittest.main()