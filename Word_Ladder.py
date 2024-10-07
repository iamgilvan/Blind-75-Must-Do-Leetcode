import collections
import unittest
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

#     Every adjacent pair of words differs by a single letter.
#     Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#     sk == endWord

# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
#TC O(N∗M)
def ladder_length(beginWord , endWord, wordList):
    if endWord not in wordList:
        return 0
    nei = collections.defaultdict(list)
    wordList.append(beginWord)
    for  word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i + 1:]
            nei[pattern].append(word)

    visit = set([beginWord])
    q = collections.deque([beginWord])
    res = 1
    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                for neiWord in nei[pattern]:
                    if neiWord not in visit:
                        visit.add(neiWord)
                        q.append(neiWord)
        res += 1
    return 0
class Test(unittest.TestCase):
    test_cases = [("hit", "cog",["hot","dot","dog","lot","log","cog"],  5),
        ( "hit", "cog", ["hot","dot","dog","lot","log"], 0)
    ]
    functions = [ladder_length]
    def test_ladder_length(self):
        for function in self.functions:
            for beginWord , endWord, wordList , result  in self.test_cases:
                expected = function(beginWord , endWord, wordList)
                assert result == expected

if __name__ == '__main__':
    unittest.main()