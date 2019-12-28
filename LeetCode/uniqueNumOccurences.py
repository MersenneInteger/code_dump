class Solution:
    def uniqueOccurrences(self, arr):

        num_map = {}
        for n in arr:
            if n not in num_map.keys():
                num_map[n] = 0
            else:
                num_map[n] += 1
        values = []
        for value in num_map.values():
            if value in values:
                return False
            values.append(value)
        return True

s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))