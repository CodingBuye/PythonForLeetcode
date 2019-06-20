class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def range_sum_of_BST(self, root, l, r):
        res = 0
        if root:
            if root.val < l:
                res += self.range_sum_of_BST(root.right, l, r)
            elif root.val > r:
                res += self.range_sum_of_BST(root.left, l, r)
            else:
                res += root.val
                res += self.range_sum_of_BST(root.left, l, r)
                res += self.range_sum_of_BST(root.right, l, r)
        return res


if __name__ == "__main__":
    node1 = TreeNode(10)
    node2 = TreeNode(5)
    node3 = TreeNode(15)
    node4 = TreeNode(3)
    node5 = TreeNode(7)
    node6 = TreeNode(18)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6

    s = Solution().range_sum_of_BST(node1, 7, 15)
    print(s)
