class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return root
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    # 迭代(超时)
    def search_bst(self, root, val):
        stack = [root]
        while stack:
            root = stack.pop()
            if root.val == val:
                return root
            else:
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)
        return None

    # 直接遍历
    def search_bst_direct(self, root, val):
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None



if __name__ == "__main__":
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(7)
    node4 = TreeNode(1)
    node5 = TreeNode(3)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    print(Solution().search_bst_direct(node1, 5))
