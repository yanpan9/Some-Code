from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n = sum(count)
        if n%2==0:
            floor, ceil = n>>1, (n>>1)+1
        else:
            floor = ceil = (n+1)>>1
        sum_ = 0
        min_, max_ = 255, 0
        mode = mode_cnt = 0
        cum_sum = median = 0
        for num,cnt in enumerate(count):
            if cnt:
                sum_ += num*cnt
                if num<min_:
                    min_ = num
                if num>max_:
                    max_ = num
                if floor>cum_sum and floor<=cum_sum+cnt:
                    median += num/2
                if ceil>cum_sum and ceil<=cum_sum+cnt:
                    median += num/2
                cum_sum += cnt
                if cnt > mode_cnt:
                    mode = num
                    mode_cnt = cnt
        return [min_, max_, sum_/n, median, mode]