from collections import deque
from typing import List

class Solution_BFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        if grid:
            m, n = len(grid), len(grid[0])
            visited = set()
            res = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j]=="1" and (i,j) not in visited:
                        visited.add((i,j))
                        self.bfs(grid,visited,i,j,m,n)
                        res += 1
        return res

    def bfs(self, grid, visited, i, j, m, n):
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        queue = deque()
        queue.append((i,j))
        while queue:
            x, y = queue.popleft()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if nx>=0 and nx<m and ny>=0 and ny<n:
                    if grid[nx][ny]=="1" and (nx, ny) not in visited:
                        visited.add((nx,ny))
                        queue.append((nx,ny))

class UnionFind:
    def __init__(self, grid, m, n):
        self.count = 0
        self.parent = list()
        self.rank = list()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent.append(i*n+j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            elif self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            else:
                self.parent[y_root] = x_root
                self.rank[x_root] += 1
            self.count -= 1

    def getCount(self):
        return self.count

class Solution_UF:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        uf = UnionFind(grid, m, n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if i+1<m and grid[i+1][j]=="1":
                        uf.union(i*n+j, i*n+n+j)
                    if j+1<n and grid[i][j+1]=="1":
                        uf.union(i*n+j, i*n+j+1)
        return uf.getCount()
