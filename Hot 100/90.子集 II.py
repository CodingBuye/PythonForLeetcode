class Solution:
    def subsets_with_dup(self, nums):
        res = []
        n = len(nums)
        nums = sorted(nums)

        def helper(i, temp):
            if temp not in res:
                res.append(temp)
            for j in range(i, n):
                helper(j+1, temp+[nums[j]])
        helper(0, [])
        return res


if __name__ == "__main__":
    arr = [4, 4, 4, 1, 4]
    print(Solution().subsets_with_dup(arr))
