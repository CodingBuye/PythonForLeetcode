class Solution:
    def findOccurrences(self, text, first, second):
        text_list = text.split()
        res = []
        for i in range(len(text_list)-2):
            if text_list[i] == first and text_list[i+1] == second:
                res.append(text_list[i+2])
        return res


if __name__ == "__main__":
    txt = "we will we will rock you"
    first = "we"
    second = "will"
    r = Solution().findOccurrences(txt, first, second)
    print(r)
