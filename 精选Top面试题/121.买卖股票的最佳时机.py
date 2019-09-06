import sys

class Solution:
    def max_profit(self, prices):
        """
        :param prices: 数组，它的第 i 个元素是一支给定股票第 i 天的价格
        :return: 你所能获取的最大利润。
        """
        min_item = sys.maxsize
        res = 0
        for price in prices:
            if price <= min_item:
                min_item = price
            else:
                if price - min_item > res:
                    res = price - min_item
        return res


if __name__ == "__main__":
    arr = [7, 1, 5, 3, 6, 4]
    print(Solution().max_profit(arr))
