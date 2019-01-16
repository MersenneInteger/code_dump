#!usr/bin/env python3

#note, with list comprehension, runtime = 84ms (10% faster than all leetcode submits)
#with for loop, runtime = 56ms (98.53% faster than all leetcode submits?)
#with slices in the list comp, runtime = 64ms (73%)

#jewels and stones
class Solution:
    def numJewelsInStones(self, J, S):
        jewels = 0
        for i in S:
            if i in J:
                jewels += 1
        #jewels = [x for x in S if x in J]
        #return len(jewels)

        #jewels = [x for x in S[:] if x in J[:]]
        #return len(jewels)
        return jewels

solution = Solution()
print(solution.numJewelsInStones('aA','aAAbbb'))