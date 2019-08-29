from functools import reduce


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        while x % 10 == 0:
            x = x // 10
        flag = -1 if x < 0 else 1
        return self.help(abs(x), flag)

    def help(self, x: int, flag: int) -> int:
        arr = []
        while x // 10 != 0:
            yushu = x % 10
            x = x // 10
            arr.append(yushu)
        arr.append(x)
        res = reduce(lambda x, y: x*10+y, arr) * flag
        return res


if __name__ == "__main__":
    x = -102300
    print(Solution().reverse(x))
