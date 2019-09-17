class Solution:
    # 解法1
    def remove_duplicates1(self, nums):
        if len(nums) <= 2:
            return len(nums)
        current = 1
        for i in range(2, len(nums)):
            if nums[i] != nums[current - 1]:
                current += 1
                nums[current] = nums[i]
        return current + 1

    # 解法2
    def remove_duplicates2(self, nums):
        if len(nums) <= 2:
            return len(nums)
        i = 2
        while i < len(nums):
            if nums[i] == nums[i-2]:
                nums.pop(i)
            else:
                i += 2
        return len(nums)


if __name__ == "__main__":
    arr1 = [1, 1, 1, 2, 2, 3]
    arr2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(Solution().remove_duplicates1(arr1))
    print(Solution().remove_duplicates2(arr2))
