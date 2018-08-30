class Solution(object):
    def flipAndInvertImage(self, A):
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] = 1 if A[i][j] == 0 else 0
            for k, l in zip(range(len(A[i])-1, -1, -1), range(len(A[i]))):
                temp = A[i][k]
                A[i][k] = A[i][l]
                A[i][l] = temp
        return A

exercise = Solution()
B = [[1,1,0],[1,0,1],[0,0,0]]
print(exercise.flipAndInvertImage(B))
