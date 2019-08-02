class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def merge_trees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t2 and not t1:
            return t2
        elif t1 and t2:
            t1.val = t1.val + t2.val
            t1.left = self.merge_trees(t1.left, t2.left)
            t1.right = self.merge_trees(t1.right, t2.right)
        return t1


if __name__ == "__main__":
    root1 = TreeNode(1)
    node1_1 = TreeNode(2)
    node1_2 = TreeNode(3)

    root1.left = node1_1
    node1_1.left = node1_2

    root2 = TreeNode(1)
    node2_1 = TreeNode(2)
    node2_2 = TreeNode(3)

    root2.right = node2_1
    node2_1.right = node2_2

    new_root = Solution().merge_trees(root1, root2)
    print(new_root.val)
