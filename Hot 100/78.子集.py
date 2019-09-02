class Solution:
    # 迭代
    def subsets1(self, nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

    # 回溯
    def subsets2(self, nums):
        res = []
        n = len(nums)

        def helper(i, temp):
            res.append(temp)
            for j in range(i, n):
                helper(j+1, temp+[nums[j]])
        helper(0, [])
        return res


if __name__ == "__main__":
    arr = [1, 2, 3]
    print(Solution().subsets1(arr))
    print(Solution().subsets2(arr))
