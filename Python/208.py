# 208. Implement Trie (Prefix Tree)

# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
from typing import Optional


class Node:
    def __init__(self, value: Optional[str] = None):
        self.children = dict()
        self.value = value
        self.end = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if node.children.get(char) == None:
                node.children[char] = Node(char)
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if node.children.get(char) == None:
                return False
            node = node.children[char]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if node.children.get(char) == None:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("test")
param_2 = obj.search("test")
param_3 = obj.startsWith("te")
param_4 = obj.startsWith("ww")
param_5 = obj.search("te")
print(param_2)
print(param_3)
print(param_4)
print(param_5)
obj.insert("a")
print(obj.startsWith("a"))
