# Definition for singly-linked list.
import unittest


class ListNode:
    def __init__(self):
        self.children  = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = ListNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = ListNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return True

class Test(unittest.TestCase):
    trie = Trie()
    assert trie.insert("apple") == None
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True
    assert trie.insert("app") == None
    assert trie.search("app") == True

if __name__ == '__main__':
    unittest.main()