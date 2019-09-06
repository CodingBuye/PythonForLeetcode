class Solution:
    def reverse_string(self, s):
        """
        :param s: list[str]
        :return: void
        """
        size = len(s)
        left = 0
        right = size-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        print(s)


if __name__ == "__main__":
    arr = ["h", "e", "l", "l", "o"]
    Solution().reverse_string(arr)
