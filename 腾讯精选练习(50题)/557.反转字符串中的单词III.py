class Solution:
    def reverse_words(self, s):
        return ' '.join(s.split(' ')[::-1])[::-1]


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print(Solution().reverse_words(s))
