
class Solution:
    def selfDividingNumbers(self, left, right):
        
        div = []
        for n in range(left, right+1):
            n_str = str(n)
            if '0' in n_str:
                continue
            isDiv = True
            for s in n_str:
                if n % int(s) != 0:
                    isDiv = False
                    break
            if isDiv:
                div.append(n)
        return div

s = Solution()
print(s.selfDividingNumbers())
                    