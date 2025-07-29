class Solution:
    def spirallyTraverse(self, mat):
        result = []
        top, bottom = 0, len(mat) - 1
        left, right = 0, len(mat[0]) - 1

        while top <= bottom and left <= right:
            # Traverse from left to right across the top row
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1

            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1

            if top <= bottom:
                # Traverse from right to left along the bottom row
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1

            if left <= right:
                # Traverse from bottom to top along the left column
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1

        return result