class Solution:
    def rotateMatrix(self, mat):
        n = len(mat)

        #Transposing the matrix
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        #Reversing each column
        for j in range(n):
            for i in range(n // 2):
                mat[i][j], mat[n - i - 1][j] = mat[n - i - 1][j], mat[i][j]

        return mat