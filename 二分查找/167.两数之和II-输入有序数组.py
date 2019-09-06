class Solution:
    # 两数之和I的解法
    def two_sum(self, numbers, target):
        """
        :param numbers: list[int]
        :param target: int
        :return: list[int]
        """
        ans = []
        dic = {}
        for (index, item) in enumerate(numbers):
            if target - item not in dic.keys():
                dic[item] = index
            else:
                ans = [dic[target-item]+1, index+1]
        return ans

    # 二分解法
    def two_sum2(self, numbers, target):
        size = len(numbers)
        left = 0
        right = size - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left+1, right+1]
        return [-1, -1]


if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    aim = 9
    print(Solution().two_sum2(arr, aim))
