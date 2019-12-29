class Solution:
    def removeVowels(self, string):
        
        return ''.join(list(filter(lambda x: x not in ['a','e','i','o','u'], string)))

s = Solution()
print(s.removeVowels('this is a string with vowels'))