from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ninf = -2**31
        array = [ninf for _ in range(k)]
        for num in nums:
            if num>array[0]:
                array[0]=num
                self.adjustHeap(array, 0, k)
        return min(array)
        
    def adjustHeap(self, array, i, length):
        key = array[i]
        while 2*i+1<length:
            ni = 2*i+1
            if ni+1<length and array[ni]>array[ni+1]:
                ni += 1
            if key > array[ni]:
                array[i] = array[ni]
                i = ni
            else:
                break
        array[i] = key