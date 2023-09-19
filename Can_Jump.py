import unittest

#time complexity O(N) : space complexity O(1)
def can_jump(nums):
    max_reach = 0  # O índice mais distante alcançável
    for i in range(len(nums)):
        if i > max_reach:
            return False  # Se não podemos alcançar o índice atual, retornamos False
        max_reach = max(max_reach, i + nums[i])  # Atualizamos o índice mais distante alcançável
    return True  # Se chegarmos até aqui, é possível alcançar o último índice


class Test(unittest.TestCase):
    test_cases = [
        ([2,3,1,1,4], True),
        ([3,2,1,0,4], False),
        ([2,0], True),
        ([0,1], False),
        ([2,0,0], True)
    ]
    functions = [can_jump]
    def test_can_jump(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()