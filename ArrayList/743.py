from typing import List 

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        times = {(u,v):w for u,v,w in times}
        inf = float("inf")
        dis_arr = [inf for _ in range(N+1)]
        dis_arr[K] = 0
        Q = set(range(1,N+1))
        while Q:
            u = self.extractMin(Q, dis_arr)
            if u == None:
                return -1
            Q.discard(u)
            for v in Q:
                if (u,v) in times and dis_arr[u]+times[(u,v)] < dis_arr[v]:
                    dis_arr[v] = dis_arr[u]+times[(u,v)]
        return max(dis_arr[1:])
    
    def extractMin(self, Q, dis_arr):
        min_idx = None
        min_val = float("inf")
        for i in Q:
            if dis_arr[i]<min_val:
                min_val = dis_arr[i]
                min_idx = i
        return min_idx