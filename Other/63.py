class Solution_Low_Space:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        path_list = [0]*n
        path_list[0] = 1
        for i in range(m):
            if obstacleGrid[i][0]:
                path_list[0] = 0
            for j in range(1,n):
                if not obstacleGrid[i][j]:
                    path_list[j] += path_list[j-1]
                else:
                    path_list[j] = 0
        return path_list[-1]

class Solution_Normal_DP:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[-1][-1]==1 or obstacleGrid[0][0]==1:
            return 0
        dp_array = [[0 for j in range(n)] for i in range(m)]
        dp_array[0][0]=1
        m_range, n_range = range(1,m), range(1,n)
        for i in m_range:
            if not obstacleGrid[i][0]:
                dp_array[i][0] = 1
            else:
                break
        for j in n_range:
            if not obstacleGrid[0][j]:
                dp_array[0][j]=1
            else:
                break
        for i in m_range:
            for j in n_range:
                if not obstacleGrid[i][j]:
                    dp_array[i][j] = dp_array[i-1][j] + dp_array[i][j-1]
        return dp_array[-1][-1]