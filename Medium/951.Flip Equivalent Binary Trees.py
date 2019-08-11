class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flip_equiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flip_equiv(root1.left, root2.left) and
                self.flip_equiv(root1.right, root2.right) or
                self.flip_equiv(root1.left, root2.right) and
                self.flip_equiv(root1.right, root2.left))


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)

    no1de = TreeNode(1)
    no2de = TreeNode(2)
    no3de = TreeNode(3)
    no4de = TreeNode(4)
    no5de = TreeNode(5)
    no6de = TreeNode(6)
    no7de = TreeNode(7)
    no8de = TreeNode(8)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node5.left = node7
    node5.right = node8

    no1de.left = no3de
    no1de.right = no2de
    no3de.right = no6de
    no2de.left = no4de
    no2de.right = no5de
    no5de.left = no8de
    no5de.right = no7de

    print(Solution().flip_equiv(node1, no1de))
