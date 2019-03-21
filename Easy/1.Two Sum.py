class Solution:
    def twoSum(self, nums, target):
        dicts = {}
        for i in range(len(nums)):
            x = nums[i]
            if x in dicts:
                return [dicts.get(x), i]
            dicts[target-x] = i

    # def twoSum(self, nums, target):
    #     for (index, x) in enumerate(nums):
    #         y = target - x
    #         # 判断y是否在x之后的列表里
    #         if y in nums[index+1:]:
    #             return [index, nums[index+1:].index(y)+index+1]


if __name__ == "__main__":
    s = Solution()
    s.twoSum([2, 7, 11, 15], 9)
