from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        array = [(0,0) for _ in range(k)]
        for key in counter:
            ele = (counter[key], key)
            if self.cmp(ele, array[0]):
                array[0] = ele
                self.adjustHeap(array, 0, k)
        res = sorted(array, key=lambda x:(-x[0], x[1]))
        return [i[1] for i in res]
    
    def cmp(self, x, y):
        if x[0]>y[0]:
            return True
        elif x[0]<y[0]:
            return False
        elif x[1]<y[1]:
            return True
        else:
            return False
    
    def adjustHeap(self, heap, i, length):
        val = heap[i]
        while 2*i+1<length:
            idx = 2*i+1
            if idx+1<length and self.cmp(heap[idx], heap[idx+1]):
                idx += 1
            if self.cmp(val, heap[idx]):
                heap[i] = heap[idx]
                i = idx
            else:
                break
        heap[i] = val