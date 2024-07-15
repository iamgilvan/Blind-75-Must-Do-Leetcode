
# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.
#TC O(n^2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in (range(len(s))):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i , i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
