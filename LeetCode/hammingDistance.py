def intToBin(num):
    powers = []
    for pow in range(255, -1,-1):
        powers.append(2 ** pow)
    binaryOutput = ''
    for power in powers:
        binaryOutput = binaryOutput + str(num // power)
        num %= power
    return binaryOutput

class Solution(object):

    def hammingDistance(self, x, y):
        xBin = intToBin(x)
        yBin = intToBin(y)
        hDist = 0
        for i in range(len(xBin)):
            if xBin[i] != yBin[i]:
                hDist += 1
        return hDist

exercise = Solution();
print(exercise.hammingDistance(1,4))