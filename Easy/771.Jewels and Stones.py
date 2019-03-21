class Solution(object):

    def numJewelsInStones(self, J: str, S: str) -> int:
        """
        遍历J，通过str的count方法计算包含J中元素的个数进行累加
        :param J: 珠宝的类型
        :param S: 所拥有的石头
        :return: 所拥有的石头中有多少颗珠宝
        """
        num = 0
        for i in J:
            num += S.count(i)
        return num


J = 'aA'
S = 'aAAbbbb'

# J = "z"
# S = "ZZ"
print(Solution().numJewelsInStones(J, S))
