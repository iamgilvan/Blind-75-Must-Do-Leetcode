from typing import List
import unittest

# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

#TC - O(n) linear SC: O(m+n)
def encode(strs: List[str]) -> str:
    r = ""
    for s in strs:
        r += str(len(s)) + "#" + s
    return r

def decode(s: str) -> List[str]:
    res = []
    idx = 0
    while idx < len(s):
        num = int(s[idx])
        initial_i = idx
        while s[idx + 1] != "#":
            idx += 1
        num = int(s[initial_i]) if initial_i == idx else int(s[initial_i:idx+1])
        word = s[idx + 2: + idx+ num + 2]
        idx = idx + 2 + num
        res.append(word)
    return res

class Test(unittest.TestCase):
    test_cases = [
        (["neet","code","love","you"]),
        (["we","say",":","yes"]),
        (["we","say",":","yes","!@#$%^&*()"])
    ]

    def test_encode_decode(self):
        for s in self.test_cases:
            enc_r = encode(s)
            dec_r = decode(enc_r)
            self.assertEqual(s, dec_r)

if __name__ == '__main__':
    unittest.main()