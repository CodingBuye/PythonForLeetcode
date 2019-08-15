class Solution:
    def findPeakElement(self, nums):
        low = 0
        high = len(nums)-1
        while low < high:
            mid = low+(high-low)//2
            if nums[mid] > nums[mid+1]:
                high = mid
            else:
                low = mid+1
        return low


if __name__ == "__main__":
    arr = [1, 2, 1, 3, 5, 6, 4]
    print(Solution().findPeakElement(arr))
