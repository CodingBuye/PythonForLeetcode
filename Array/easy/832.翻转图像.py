class Solution:
    def flipAndInvertImage(self, A):
        for index in range(len(A)):
            temp = []
            for i in reversed(A[index]):
                if i == 0:
                    i = 1
                else:
                    i = 0
                temp.append(i)
            A[index] = temp
        return A


if __name__ == "__main__":
    arr = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(Solution().flipAndInvertImage(arr))
