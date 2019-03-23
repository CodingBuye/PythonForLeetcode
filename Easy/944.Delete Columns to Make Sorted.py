class Solution:
    def minDeletionSize(self, A):
        str_len = len(A[0])
        possible_length = 0
        for i in range(str_len):
            old_s = ""
            for s in A:
                old_s += s[i]
            new_s = "".join(sorted(old_s))
            if old_s != new_s:
                possible_length += 1
        return possible_length


class Solution1:
    def minDeletionSize(self, A):
        return sum(list(col) != sorted(col) for col in zip(*A))


class Solution2:
    def minDeletionSize(self, A):
        return sum(any(a > b for a, b in zip(col, col[1:])) for col in zip(*A))


size1 = ["cba", "daf", "ghi"]
# print(Solution().minDeletionSize(size1))
#
# size2 = ["a", "b"]
# print(Solution().minDeletionSize(size2))
#
# size3 = ["zyx", "wvu", "tsr"]
# print(Solution().minDeletionSize(size3))

for column in zip(*size1):
    print(column)

# ('c', 'd', 'g')
# ('b', 'a', 'h')
# ('a', 'f', 'i')
