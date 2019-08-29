class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    # 递归
    def preorder(self, root: Node):
        if root:
            res = [root.val]
            if root.children:
                for child in root.children:
                    res.extend(self.preorder(child))
            return res
        return []

    # 迭代
    def pre_order(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                reversed_children = reversed(node.children)
                for child in reversed_children:
                    stack.append(child)
        return res


if __name__ == "__main__":
    node5 = Node(5, None)
    node6 = Node(6, None)

    node4 = Node(4, None)
    node2 = Node(2, None)

    node3 = Node(3, [node5, node6])

    node1 = Node(1, [node3, node2, node4])
    print(Solution().pre_order(node1))
