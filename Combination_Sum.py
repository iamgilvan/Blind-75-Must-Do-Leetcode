import unittest
#Tempo de complexidade O(2^n): space O(n * k)
def combination_sum(arr, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(arr)):
            # Evite duplicatas, começando a partir do índice atual
            if i > start and arr[i] == arr[i - 1]:
                continue
            backtrack(i, target - arr[i], path + [arr[i]])

    result = []
    arr.sort()  # Ordenar o conjunto, se desejar
    backtrack(0, target, [])
    return result

#O(n * target)
def combination_sum_with_combinations(arr, target):
    dp = [[] for _ in range(target + 1)]
    dp[0].append([])  # Inicialização: Uma combinação vazia para obter zero.

    for num in arr:
        for i in range(num, target + 1):
            for prev_combination in dp[i - num]:
                new_combination = prev_combination + [num]
                dp[i].append(new_combination)

    return dp[target]

class Test(unittest.TestCase):
    test_cases = [
        ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
        ([2], 1, []),
        ([2,3,6,7], 7, [[2,2,3],[7]]),
        ([2,3], 5, [[2,3]]),
    ]
    functions = [combination_sum, combination_sum_with_combinations]
    def test_combination_sum(self):
        for function in self.functions:
            for arr, target, expected in self.test_cases:
                result = function(arr, target)
                assert result == expected

if __name__ == '__main__':
    unittest.main()