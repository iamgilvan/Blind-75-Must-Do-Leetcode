import unittest
import math

def productExceptSelf(nums):
    res = [] 
    for i in range(len(nums)):
        temp = nums[:i]
        temp += nums[i+1:]
        if 0 in temp:
            res.append(0)
        else:
            res.append(math.prod(temp))
    return res

#TC O(n)
#TS O(1)
def productExceptSelf_G(nums):
    res = [1]  * (len(nums))
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix =1 
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *=nums[i]
    return res

class Test(unittest.TestCase):
    test_cases = [
        ([1,2,3,4], [24,12,8,6]),
        ([-1,1,0,-3,3], [0,0,9,0,0]),
    ]
    functions = [productExceptSelf, productExceptSelf_G]
    def test_productExceptSelf(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()