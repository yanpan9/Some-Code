from typing import List

class Solution_BF:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        subs = [gas[i]-cost[i] for i in range(length)]
        if sum(subs)<0:
            return -1
        else:
            for idx,num in enumerate(subs):
                if num<0:
                    continue
                else:
                    sum_ = 0
                    for i in range(length):
                        sum_ += subs[(idx+i)%length]
                        if sum_<0:
                            break
                    else:
                        return idx
            else:
                return -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = start = cur = 0
        length = len(gas)
        for i in range(length):
            sub = gas[i]-cost[i]
            cur += sub
            if cur < 0:
                start = i+1
                total += cur
                cur = 0
        total += cur
        return -1 if total<0 else start