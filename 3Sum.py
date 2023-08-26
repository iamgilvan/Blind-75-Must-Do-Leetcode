import unittest

# Time Complexity: O(N^3), Space Complexity: O(1)
def three_sum(nums):
    if len(nums) < 2:
        return []
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if (nums[k] + nums[j] + nums[i]) == 0:
                    arr = [nums[k], nums[j], nums[i]]
                    arr.sort()
                    if arr not in result:
                        result.append(arr)
    return result

# Time Complexity: O(N^2), Space Complexity: O(1)
def three_sum_better(nums):
    nums.sort()  # Ordenar a lista de números
    result = []

    for i in range(len(nums) - 2):
        # evitar numeros duplicados
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Evitar elementos duplicados

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # evitar numeros duplicados
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # evitar numeros duplicados
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result

class Test(unittest.TestCase):
    test_cases = [
        ([0,0,0], [[0,0,0]]),
        ([0,1,0], []),
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ]
    functions = [three_sum, three_sum_better]
    def test_three_sum(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()