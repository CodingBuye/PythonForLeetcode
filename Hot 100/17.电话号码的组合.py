class Solution(object):
    def letter_combinations(self, digits):
        """
        :param digits: 输入的数字组合
        :return: 可能的字母组合
        """
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def combinations(combination, next_digit):
            if len(next_digit) == 0:
                output.append(combination)
            else:
                for letter in phone[next_digit[0]]:
                    combinations(combination+letter, next_digit[1:])

        output = []
        if digits:
            combinations("", digits)
        return output


if __name__ == "__main__":
    s = "23"
    print(Solution().letter_combinations(s))
