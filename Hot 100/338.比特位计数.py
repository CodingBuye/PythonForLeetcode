class Solution:
    def countBits(self, num):
        """
        :param num: 非负整数
        :return: 数组，0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目
        """
        res = [0]
        for i in range(1, num+1):
            if i % 2 == 0:
                res.append(res[i//2])
            else:
                res.append(res[i-1]+1)
        return res


if __name__ == "__main__":
    num1 = 2
    num2 = 5
    print(Solution().countBits(num1))
    print(Solution().countBits(num2))
