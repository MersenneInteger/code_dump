class Solution(object):
    def sortArrayByParity(self, A):
        
        e = [i for i in A if i%2==0]
        o = [i for i in A if i%2!=0]
        return e + o