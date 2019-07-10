from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)-2
        n = len(dungeon[0])-2
        dungeon[-1][-1] = max(1, 1-dungeon[-1][-1])
        for i in range(m,-1,-1):
            dungeon[i][-1] = self.calculate(dungeon[i+1][-1]-dungeon[i][-1])
        for j in range(n,-1,-1):
            dungeon[-1][j] = self.calculate(dungeon[-1][j+1]-dungeon[-1][j])
        for i in range(m,-1,-1):
            for j in range(n,-1,-1):
                right = self.calculate(dungeon[i][j+1]-dungeon[i][j]) 
                bottom = self.calculate(dungeon[i+1][j]-dungeon[i][j])
                dungeon[i][j] = min(right, bottom)
        return dungeon[0][0]
    
    def calculate(self, value):
        return 1 if value<=0 else value