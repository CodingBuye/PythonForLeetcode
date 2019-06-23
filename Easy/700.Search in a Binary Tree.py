class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def search_bst(self, root, val):
        if root:
            if root.val == val:
                return root
            elif root.val > val:
                return self.search_bst(root.left, val)
            elif root.val < val:
                return self.search_bst(root.right, val)
            else:
                return None
        return None


if __name__ == "__main__":
    node1 = TreeNode(18)
    node2 = TreeNode(2)
    node3 = TreeNode(22)
    node4 = TreeNode(63)
    node5 = TreeNode(84)

    node1.left = node2
    node1.right = node3
    node2.right = node4
    node4.right = 84

    res = Solution().search_bst(node1, 63)
    print(res.val)
