from math import sqrt

class Solution_DP:
    def divisorGame(self, N: int) -> bool:
        array = [False for _ in range(N+1)]
        if N<2:
            return False
        else:
            array[2]=True
            for i in range(3, N+1):
                for j in range(1, int(sqrt(i))+1):
                    if i%j==0 and array[i-j]==False:
                        array[i] = True
                        break
            return array[-1]

class Solution_MathGame:
	def divisorGame(self, N: int) -> bool:
		return N%2==0