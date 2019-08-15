class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums):
        max_value = nums[0]
        max_index = 0
        for i in range(1, len(nums)):
            if nums[i] > max_value:
                max_value = nums[i]
                max_index = i
        root = TreeNode(max_value)
        if nums[:max_index]:
            root.left = self.constructMaximumBinaryTree(nums[:max_index])
        if nums[max_index+1:]:
            root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        return root


if __name__ == "__main__":
    arr = [3, 2, 1, 6, 0, 5]
    r = Solution().constructMaximumBinaryTree(arr)
    print(r.val)
    if r.left:
        print(r.left.val)
    if r.right:
        print(r.right.val)
