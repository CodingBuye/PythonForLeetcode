class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kth_smallest(self, root, k):
        """
        :param root: TreeNode
        :param k: int
        :return: int
        """
        def in_order(root):
            if not root:
                return []
            ans = []
            if root.left:
                ans += in_order(root.left)
            ans.append(root.val)
            if root.right:
                ans += in_order(root.right)
            return ans

        res = in_order(root)
        return res[k - 1]


if __name__ == "__main__":
    node1 = TreeNode(3)
    node2 = TreeNode(1)
    node3 = TreeNode(4)
    node4 = TreeNode(2)
    node1.left = node2
    node1.right = node3
    node2.right = node4

    print(Solution().kth_smallest(node1, 1))
