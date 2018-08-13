class TireNode:
    def __init__(self, val):
        self.val = val
        self.next = {}

    def __str__(self):
        return "val:{val},next:{next}".format(val=self.val, next=self.next)

    def __repr__(self):
        return self.__str__()


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TireNode(0)

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        # init param
        i = 0
        node = self.root
        while i < len(key):
            char = key[i]
            if not node.next.get(char):
                node.next[char] = TireNode(0)
            # update node
            node = node.next[char]
            # update index
            i = i + 1
        # reach the leaf
        node.val = val

    def dfs(self, root):
        if root.next == {}:
            return root.val
        result = root.val
        for i, v in root.next.items():
            result += self.dfs(v)
        return result

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for char in prefix:
            if not node.next.get(char):
                return 0
            node = node.next.get(char)
        print(node)
        return self.dfs(node)



# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert('apple', 3)
param_2 = obj.sum('app')
print(param_2)
obj.insert('app', 2)
param_2 = obj.sum('ap')
print(param_2)
