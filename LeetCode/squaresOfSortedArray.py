#squares of sorted array
class Solution:
    def sortedSquares(self, A):
        
        #224 ms, 100% faster
        return sorted([x*x for x in A])

        #248 ms, still 100% faster
#        sortedA = []
#        for i in A:
#            sortedA.append(i*i)
#        sortedA.sort()
#        return sortedA

s = Solution()
l = [-7,-3,2,3,11]
print(s.sortedSquares(l))