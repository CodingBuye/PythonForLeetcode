class Solution:
    def convert(self, s, numRows):
        pass


s = "PAYPALISHIRING"
s1 = [s[x] for x in range(0, len(s), 4)]
s2 = [s[x] for x in range(1, len(s), 2)]
s3 = [s[x] for x in range(2, len(s), 4)]
print(s1)
print(s2)
print(s3)
