from collections import Counter
from typing import List

class Solution_MaxHeap:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        array = list(counter.items())
        length = len(array)
        res = list()
        for i in range((length-1)//2, -1, -1):
            self.adjustHeap(array, i, length, key=lambda x:x[1])
        for _ in range(k):
            res.append(array[0][0])
            length -= 1
            array[0] = array[length]
            self.adjustHeap(array, 0, length, key=lambda x:x[1])
        return res
            
    def adjustHeap(self, heap, i, length, key=lambda x:x):
        val = heap[i]
        while 2*i+1<length:
            idx = 2*i+1
            if idx+1<length and key(heap[idx+1])>key(heap[idx]):
                idx += 1
            if key(heap[idx])>key(val):
                heap[i] = heap[idx]
                i = idx
            else:
                break
        heap[i] = val

class Solution_MinHeap:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        array = [(0,0) for _ in range(k)]
        for key in counter:
            if counter[key]>array[0][0]:
                array[0] = (counter[key], key)
                self.adjustHeap(array, 0, k)
        res = sorted(array, key=lambda x:x[0], reverse=True)
        return [i[1] for i in res]
            
    def adjustHeap(self, heap, i, length):
        val = heap[i]
        while 2*i+1<length:
            idx = 2*i+1
            if idx+1<length and heap[idx+1]<heap[idx]:
                idx += 1
            if heap[idx]<val:
                heap[i] = heap[idx]
                i = idx
            else:
                break
        heap[i] = val