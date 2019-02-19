class Solution:
    def peakIndexInMountainArray(self, A):
        peak = A[0]
        for i in range(len(A)):
            if A[i] > peak:
                peak = A[i]
                index = i
        return index

s = Solution()
print(s.peakIndexInMountainArray([0,1,0]))