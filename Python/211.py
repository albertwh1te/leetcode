# 211. Add and Search Word - Data structure design
# Medium

# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A
# . means it can represent any one letter.

# Example:

# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.
from typing import List, Any, Dict
from collections import defaultdict


class Node(object):
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_word = defaultdict(Node)


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.root
        for char in word:
            current = current.children[char]
        current.is_word = True


    def search_helper(self, word: str, current: Node) -> bool:


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.search_helper(word,0, self.root)


obj = WordDictionary()
obj.addWord('bad')
obj.addWord('bac')
obj.addWord('dad')
obj.addWord('mad')
assert obj.search('bad') == True
assert obj.search('pad') == False
assert obj.search('.ad') == True
assert obj.search('b..') == True

# ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
# [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]

# output: [null,null,null,null,null,true,false,null,true,false,false,true,true,true]
# expect: [null,null,null,null,null,false,false,null,true,true,false,false,true,false]

obj = WordDictionary()
obj.addWord('a')
obj.addWord('at')
obj.addWord('and')
obj.addWord('an')
obj.addWord('add')
assert obj.search('a') == False
assert obj.search('.at') == False
obj.addWord('bat')
assert obj.search('.at') == True
assert obj.search('an.') == True
assert obj.search('a.d.') == False
assert obj.search('b.') == False
assert obj.search('a.d') == True
assert obj.search('.') == True
assert obj.search('..') == True
assert obj.search('...') == True
