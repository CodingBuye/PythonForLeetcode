class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归的方法
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth)+1

    # 迭代的方法
    def max_depth(self, root: TreeNode) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack:
            current_depth, root = stack.pop()
            depth = max(current_depth, depth)
            if root.left:
                stack.append((current_depth+1, root.left))
            if root.right:
                stack.append((current_depth+1, root.right))
        return depth


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
    print(Solution().max_depth(node1))
