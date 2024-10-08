import unittest
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return true if you can finish all courses. Otherwise, return false.
#TC O(V + E), #EC O(V + E)  V = numCourses E = prerequisites
def course_schedule(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]  # graph
    visited = [0] * numCourses  # 0: not visited, 1: visiting, 2: visited

    # build the graph
    for course, prerequisite in prerequisites:
        graph[course].append(prerequisite)

    def has_cycle(course):
        if visited[course] == 1: #has cycle
            return True
        if visited[course] == 2: #visited
            return False
        visited[course] = 1 # marked as visiting

        for preReq in graph[course]:
            if has_cycle(preReq):
                return True
        visited[course] = 2 # marked as visited
        return False
    # check if there is cycle in each course
    for i in range(numCourses):
        if has_cycle(i):
            return False
    return True
class Test(unittest.TestCase):
    test_cases = [
        (2, [[1,0]], True),
        (2, [[1,0],[0,1]], False),
        (3, [[1,0],[0,2],[2,1]], False)
    ]
    functions = [course_schedule]
    def test_course_schedule(self):
        for function in self.functions:
            for courseN, arr, expected in self.test_cases:
                result = function(courseN, arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()