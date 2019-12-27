class Solution:
    def subtractProductAndSum(self, n):
        
        digits = []
        while n >= 1:
            digits.append(n % 10)
            n //= 10
        prod = 1
        for i in digits:
            prod *= i
        return prod - sum(digits)

s = Solution()
print(s.subtractProductAndSum(234))
