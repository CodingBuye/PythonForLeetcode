class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.sum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.sum += root.val
            root.val = self.sum
            self.bstToGst(root.left)
        return root


if __name__ == "__main__":
    node1 = TreeNode(4)
    node2 = TreeNode(1)
    node3 = TreeNode(6)
    node4 = TreeNode(0)
    node5 = TreeNode(2)
    node6 = TreeNode(5)
    node7 = TreeNode(7)
    node8 = TreeNode(3)
    node9 = TreeNode(8)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.right = node8
    node7.right = node9

    print(Solution().bstToGst(node1).val)
