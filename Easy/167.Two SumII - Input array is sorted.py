class Solution:
    def twoSum(self, numbers, target):
        res = []
        first_index = 0
        last_index = len(numbers)-1
        for i in range(len(numbers)):
            if numbers[i] > target:
                last_index = i
                break
        while first_index < last_index:
            if numbers[first_index]+numbers[last_index] == target:
                res.append(first_index+1)
                res.append(last_index+1)
                break
            elif numbers[first_index] + numbers[last_index] < target:
                first_index += 1
            else:
                last_index -= 1
        return res


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
