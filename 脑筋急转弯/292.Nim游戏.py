class Solution:
    def can_win_nim(self, n):
        """
        :param n: int
        :return: bool
        """
        return n % 4


if __name__ == "__main__":
    n = 4
    print(Solution().can_win_nim(n))
