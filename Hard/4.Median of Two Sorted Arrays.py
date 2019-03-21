class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        if length % 2 == 0:
            return (nums1[length//2]+nums1[length//2-1])/2
        else:
            return nums1[length//2]


nums1 = [1, 2]
nums2 = [3, 4]
s = Solution().findMedianSortedArrays(nums1, nums2)
print(s)
