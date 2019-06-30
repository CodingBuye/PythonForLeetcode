class Solution:
    def sortArrayByParityII(self, A):
        i = 0
        j = 1
        l = len(A)
        while i < l and j < l:
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 2
            else:
                j += 2
        return A


if __name__ == "__main__":
    arr = [4, 2, 5, 7]
    print(Solution().sortArrayByParityII(arr))
