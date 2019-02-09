#reverse vowels
class Solution:
    def reverseVowels(self, s):

        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        v = [x for x in s if x.lower() in vowels]
        n = []
        for i in s:
            if i.lower() in vowels:
                n.append(v.pop())
            else:
                n.append(i)
        return ''.join(n)

sol = Solution()
print(sol.reverseVowels('aA'))
        