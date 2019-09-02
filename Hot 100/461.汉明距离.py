class Solution(object):
    def hamming_distance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


if __name__ == "__main__":
    x = 1
    y = 4
    print(Solution().hamming_distance(x, y))
