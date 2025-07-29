from typing import List
class Solution:
    def sumDiagonal(self, N : int , M : List[List[int]] ) -> int :
        total = 0
        for i in range (N):
            total += M[i][i]
        return total