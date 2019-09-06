class Solution:
    def intersection(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        res = []
        if len1 < len2:
            for n in nums1:
                if n in nums2 and n not in res:
                    res.append(n)
        else:
            for n in nums2:
                if n in nums1 and n not in res:
                    res.append(n)
        return res


if __name__ == "__main__":
    n1 = [4, 9, 5]
    n2 = [9, 4, 9, 8, 4]
    print(Solution().intersection(n1, n2))
