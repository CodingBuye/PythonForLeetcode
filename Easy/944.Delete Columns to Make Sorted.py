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


size1 = ["cba", "daf", "ghi"]
print(Solution().minDeletionSize(size1))

size2 = ["a", "b"]
print(Solution().minDeletionSize(size2))

size3 = ["zyx", "wvu", "tsr"]
print(Solution().minDeletionSize(size3))
