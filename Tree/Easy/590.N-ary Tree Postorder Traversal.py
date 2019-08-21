class Node:
    def __init__(self, x, children):
        self.val = x
        self.children = children


class Solution:
    def postorder(self, root):
        res = []
        if root:
            if root.children:
                for child in root.children:
                    res += self.postorder(child)
                res.append(root.val)
            else:
                res.append(root.val)
        return res

