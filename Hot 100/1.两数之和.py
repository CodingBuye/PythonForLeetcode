class Solution:
    def two_sum(self, nums, target):
        dic = {}
        for (index, item) in enumerate(nums):
            if target-item not in dic.keys():
                dic[item] = index
            else:
                return [dic[target-item], index]
        return []


if __name__ == "__main__":
    num = [2, 7, 11, 15]
    aim = 9
    print(Solution().two_sum(num, aim))
