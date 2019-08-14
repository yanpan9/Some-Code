from typing import List

class Solution_NormalDP:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m, n = len(coins)+1, amount+1
        inf = 2**32-1
        array = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            array[i][0]=0
        for j in range(1, n):
            array[0][j]=inf
        for i in range(1, m):
            for j in range(1,n):
                val = coins[i-1]
                if j<val:
                    array[i][j]=array[i-1][j]
                else:
                    array[i][j]=min(array[i][j-val]+1, array[i-1][j])
        res = array[-1][-1]
        return -1 if res==inf else res

class Solution_DP:
	def coinChange(self, coins: List[int], amount: int) -> int:
		n, inf = amount+1, 2**32-1
		array = [inf for _ in range(n)]
		array[0] = 0
		for i in range(1, n):
			for coin in coins:
				if i>=coin:
					if 1+array[i-coin]<array[i]:
						array[i] = 1+array[i-coin]
		res = array[-1]
		return -1 if res==inf else res