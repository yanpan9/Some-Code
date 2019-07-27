from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hasht = {j:i for i,j in enumerate(list1)}
        sum_, res = 2**31-1, dict()
        for idx, ele in enumerate(list2):
            if ele in hasht and idx+hasht[ele]<=sum_:
                sum_ = idx+hasht[ele]
                res[ele]=sum_
                
        return [key for key in res if res[key]==sum_]