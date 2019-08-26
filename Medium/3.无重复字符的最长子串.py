class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        left = 0
        lookup = set()
        cur_len = 0
        max_len = 0
        for i in range(len(s)):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                cur_len -= 1
                left += 1
                if max_len < cur_len:
                    max_len = cur_len
            lookup.add(s[i])
        return max_len


if __name__ == "__main__":
    a = "pwwkew"
    print(Solution().lengthOfLongestSubstring(a))
