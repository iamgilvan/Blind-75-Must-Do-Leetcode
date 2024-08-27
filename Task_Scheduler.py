from collections import Counter
import heapq
import unittest

# You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

# ​Return the minimum number of intervals required to complete all tasks.

#TC O(n)
#SC O(n)
def task_scheduler(tasks, n):
    # Count the frequency of each task
    frequencies = Counter(tasks)
    # Sort the frequencies in descending order
    frequencies = sorted(frequencies.values(), reverse=True)
    # The maximum frequency
    max_freq = frequencies[0]
    # Calculate the maximum possible idle time
    idle_time = (max_freq - 1) * n
    # Reduce idle time based on the remaining tasks
    for freq in frequencies[1:]:
        idle_time -= min(max_freq - 1, freq)
    # Idle time can't be negative
    idle_time = max(0, idle_time)
    # Total time is the sum of tasks and the remaining idle time
    return len(tasks) + idle_time

class Test(unittest.TestCase):
    test_cases = [
        (["A","A","A","B","B","B"], 2, 8),
        (["A","C","A","B","D","B"], 1, 6),
        (["A","A","A", "B","B","B"], 3, 10),
    ]
    functions = [task_scheduler]
    def test_task_scheduler(self):
        for function in self.functions:
            for tasks, k, expected in self.test_cases:
                result = function(tasks, k)
                assert result == expected

if __name__ == '__main__':
    unittest.main()