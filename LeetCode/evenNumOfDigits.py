class Solution:
    def findNumbers(self, nums):

        even_digits = list(filter(lambda x: len(str(x)) % 2 == 0, nums))
        return len(even_digits)

#        even_digits = 0
        
#        for num in nums:
#            if len(str(num)) % 2 == 0:
#                even_digits += 1
#        return even_digits

s = Solution()
print(s.findNumbers([22,11]))