class Solution:
    def peakIndexInMountainArray(self, A):
        low = 0
        high = len(A)-1
        while low <= high:
            mid = low + (high-low) // 2
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid-1] < A[mid] < A[mid+1]:
                low = mid + 1
            elif A[mid-1] > A[mid] > A[mid+1]:
                high = mid - 1
        return -1


if __name__ == "__main__":
    arr = [0, 2, 1, 0]
    print(Solution().peakIndexInMountainArray(arr))
