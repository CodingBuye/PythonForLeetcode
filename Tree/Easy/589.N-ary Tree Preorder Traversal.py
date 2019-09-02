class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root):
        res = []
        if root:
            res.append(root.val)
            if root.children:
                for child in root.children:
                    res += self.preorder(child)
        return res
