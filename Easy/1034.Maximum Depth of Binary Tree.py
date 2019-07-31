class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        depth = 0
        leftDepth = 0
        rightDepth = 0
        if root:
            depth += 1
        if root.left:
            leftDepth = self.maxDepth(root.left)
        if root.right:
            rightDepth = self.maxDepth(root.right)
        return depth+leftDepth if leftDepth > rightDepth else depth+rightDepth


if __name__ == "__main__":
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3

    node3.left = node4
    node3.right = node5

    print(Solution().maxDepth(node1))
