class Solution:
    def commonChars(self, A):
        res = []
        s = A[0]

        for c in s:
            n = 0
            for i in range(1, len(A)):
                if c not in A[i]:
                    break
                A[i] = A[i].replace(c, '', 1)
                n += 1
            if n == len(A)-1:
                res.append(c)
        return res


if __name__ == "__main__":
    arr = ['bella', 'label', 'roller']
    print(Solution().commonChars(arr))
