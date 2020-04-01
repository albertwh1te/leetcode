# 648. Replace Words

# In English, we have a concept called root,
# which can be followed by some other words to form another longer word
# - let's call this word successor.
# For example, the root an, followed by other, which can form another word another.

# Now, given a dictionary consisting of many roots and a sentence.
# You need to replace all the successor in the sentence with the root forming it.
# If a successor has many roots can form it, replace it with the root with the shortest length.

# You need to output the sentence after the replacement.

# Example 1:

# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
from typing import Optional, List


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


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        if len(dict) == 0 or len(sentence) == 0:
            return sentence
        trie = Trie()
        for root in dict:
            trie.insert(root)
        results = ""
        words = sentence.split(" ")
        for word in words:
            tmp = ""
            for char in word:
                tmp += char
                if trie.search(tmp):
                    break
                elif not trie.startsWith(tmp):
                    tmp = word
                    break
            results += tmp + " "
        return results[:-1]


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.replaceWords)
    t.equal(
        "the cat was rat by the bat",
        ["cat", "bat", "rat"],
        "the cattle was rattled by the battery",
    )
