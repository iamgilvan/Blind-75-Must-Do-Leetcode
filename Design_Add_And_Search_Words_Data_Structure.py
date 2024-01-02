# Definition for singly-linked list.
import unittest


class Node:
    def __init__(self):
        self.children  = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
     #O(N)
    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
        current.is_end_of_word = True
    #O(N * L)
    def search(self, word: str) -> bool:
        return self._search(word, self.root)

    def _search(self, word, node):
        for i, char in enumerate(word):
            if char == '.':
                for child in node.children.values():
                    if self._search(word[i + 1:], child):
                        return True
                return False
            elif char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

class Test(unittest.TestCase):
    wordDictionary = WordDictionary()
    assert wordDictionary.addWord("bad") == None
    assert wordDictionary.addWord("dad") == None
    assert wordDictionary.addWord("mad") == None
    assert wordDictionary.search("pad") == False
    assert wordDictionary.search("bad") == True
    assert wordDictionary.search(".ad") == True
    assert wordDictionary.search("b..") == True

if __name__ == '__main__':
    unittest.main()