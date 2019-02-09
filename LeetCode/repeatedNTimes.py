#n-repeated element
class Solution:
    def repeatedNTimes(self, A):
        freq = {}
        for i in A:
            if i in freq.keys():
                freq[i] += 1
            else:
                freq[i] = 1
        key = list(freq.keys())
        val = list(freq.values())
        m = max(val)
        return key[val.index(m)]

s = Solution()
l = [2,1,2,5,3,2]
k = [1,1,1,2]
print(s.repeatedNTimes(l))