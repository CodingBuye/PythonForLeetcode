class Solution:

    def maxArea(self, height):

        max_area = 0
        start = 0
        end = len(height)-1
        while start < end:
            max_area = max(max_area, (end - start) * min(height[start], height[end]))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return max_area


if __name__ == "__main__":
    s = Solution()
    max_area = s.maxArea([2,3,10,5,7,8,9])
    print(max_area)
