import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        if m<=1: return 0
        else:
            n = len(heightMap[0])
            if n<=1:return 0
            else:
                flags = [[0 for _ in range(n)] for _ in range(m)]
                pq = list()
                res = 0
                dirs = ((0,1), (1,0), (0,-1), (-1,0))
                for i in range(n):
                    heapq.heappush(pq, (heightMap[0][i], 0, i))
                    heapq.heappush(pq, (heightMap[-1][i], m-1, i))
                    flags[0][i] = 1
                    flags[-1][i] = 1
                for j in range(1, m-1):
                    heapq.heappush(pq, (heightMap[j][0], j, 0))
                    heapq.heappush(pq, (heightMap[j][-1], j, n-1))
                    flags[j][0] = 1
                    flags[j][-1] = 1
                while pq:
                    h, x, y = heapq.heappop(pq)
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if nx>=0 and nx<m and ny>=0 and ny<n:
                            if flags[nx][ny]:
                                continue
                            else:
                                if heightMap[nx][ny]<h:
                                    res += h-heightMap[nx][ny]
                                    heightMap[nx][ny] = h
                                heapq.heappush(pq, (heightMap[nx][ny], nx, ny))
                                flags[nx][ny] = 1
                return res