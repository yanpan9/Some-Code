from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length, count = len(digits), 0
        digits[-1] += 1
        for i in range(length-1, -1, -1):
            digits[i] += count
            if digits[i]<10:
                break
            else:
                count, val = divmod(digits[i], 10)
                digits[i] = val
        else:
            if count:
                digits.insert(0,count)
        return digits