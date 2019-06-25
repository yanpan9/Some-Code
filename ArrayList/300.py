class Solution_DP:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        len_dict = {0:[float("-inf")]}
        for num in nums:
            key, flag = res, True
            while flag:
                for i in len_dict[key]:
                    if num>i:
                        key += 1
                        if key in len_dict:
                            len_dict[key].append(num)
                        else:
                            len_dict[key]= [num]
                        flag = False
                        break
                else:
                    key -= 1
            res = max(res, key)
        return res

class Solution_Binary:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.tail = list()
        self.length = 0
        for num in nums:
            order = self.binarySearch(num)
            #order = bisect.bisect_left(self.tail, num)
            if order==self.length:
                self.tail.append(num)
                self.length += 1
            else:
                self.tail[order]=num
        return self.length
        
    def binarySearch(self, num):
        if self.length:
            low, high = 0, self.length-1
            while low<= high:
                mid = (low+high)//2
                if self.tail[mid]==num:
                    return mid
                elif self.tail[mid]<num:
                    low = mid+1
                else:
                    high = mid-1
            return low
        else:
            return 0