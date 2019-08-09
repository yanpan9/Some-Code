from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = list()
        m = len(matrix)
        if m:
            n = len(matrix[0])
            if n:
                up, bot = 0, m-1
                left, right = 0, n-1
                while up<=bot and left<=right:
                    for j in range(left, right+1):
                        res.append(matrix[up][j])
                    up += 1
                    if up>bot: break
                    for i in range(up, bot+1):
                        res.append(matrix[i][right])
                    right -= 1
                    if right<left: break
                    for j in range(right, left-1, -1):
                        res.append(matrix[bot][j])
                    bot -= 1
                    if bot<up: break
                    for i in range(bot, up-1, -1):
                        res.append(matrix[i][left])
                    left += 1
                    if left>right: break
        return res
                