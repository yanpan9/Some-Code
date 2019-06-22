class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Traverse row
        for i in range(n//2):
            # Traverse element which need to be rotate
            # in the row
            for j in range(i, n-1-i):
                cache = matrix[i][j]
                for _ in range(4):
                    i, j = j, n-1-i
                    cache, matrix[i][j] = matrix[i][j], cache