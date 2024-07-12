import unittest

#TC O(n)
#TS O(n)
def daily_temperatures(arr):
    result = [0] * len(arr)
    stack = [] # pair: [temp, index]
    for i, t in enumerate(arr):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            result[stackInd] = (i - stackInd)
        stack.append([t, i])
    return result

#TC O(n^2)
#TS O(n)
def daily_temperatures_brute_force(arr):
    result = [0] * len(arr)
    for i in range(len(arr)-1):
        j=i
        count=0
        while j<len(arr) and arr[j]<=arr[i]:
            count+=1
            j+=1
        if j<len(arr):
            result[i] = count
    return result

class Test(unittest.TestCase):
    test_cases = [
        ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
        ([30,40,50,60], [1,1,1,0]),
        ([30,60,90], [1,1,0])
    ]
    functions = [daily_temperatures, daily_temperatures_brute_force]
    def test_daily_temperatures(self):
        for function in self.functions:
            for n, expected in self.test_cases:
                result = function(n)
                assert result == expected

if __name__ == '__main__':
    unittest.main()