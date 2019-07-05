from typing import List
from data_structure import ListNode

class Solution:
    def sortArray_Insert(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(1, length):
            for j in range(i):
                if nums[j]>nums[i]:
                    nums.insert(j, nums.pop(i))
                    break
        return nums
        
    def sortArray_Bubble(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for _ in range(1, length):
            flag = True
            for j in range(1, length):  
                if nums[j]<nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    flag = False
            if flag:
                break
        return nums

    def sortArray_QuickSort(self, nums: List[int]) -> List[int]:
        if nums:
            length = len(nums)
            self.quickSort(nums, 0, length-1)
        return nums
        
    def quickSort(self, nums, low, high):
        if low<high:
            pivot_idx = self.partion(nums, low, high)
            self.quickSort(nums, low, pivot_idx-1)
            self.quickSort(nums, pivot_idx+1, high)
    
    def partion(self, nums, low, high):
        pivot = nums[low]
        while low<high:
            while low<high and nums[high]>=pivot:
                high -= 1
            nums[low]=nums[high]
            while low<high and nums[low]<=pivot:
                low += 1
            nums[high]=nums[low]
        nums[low] = pivot
        return low

    def sortArray_Select(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length-1):
            min_idx = i
            for j in range(i+1, length):
                if nums[j]<nums[min_idx]:
                    min_idx = j
            if min_idx==i:
                continue
            else:
                nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums

    def sortArray_Heap(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length//2-1, -1, -1):
            self.heapAdjust(nums, i, length)
        for i in range(length, 0, -1):
            nums[0], nums[i-1] = nums[i-1], nums[0]
            self.heapAdjust(nums, 0, i-1)
        return nums
    
    def heapAdjust(self, nums, idx, length):
        key = nums[idx]
        c_idx = idx*2+1
        while c_idx<length:
            if c_idx+1<length and nums[c_idx+1]>nums[c_idx]:
                c_idx+=1
            if nums[c_idx]>key:
                nums[idx]=nums[c_idx]
                idx,c_idx = c_idx, c_idx*2+1
            else:
                break
        nums[idx]=key

    def sortArray_Merging(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length<=1:
            return nums
        else:
            mid = length//2
            left = self.sortArray_Merging(nums[:mid])
            right = self.sortArray_Merging(nums[mid:])
            return self.merge2List(left, right)
    
    def merge2List(self, nums1, nums2):
        len_1, len_2 = len(nums1), len(nums2)
        i_1, i_2 = 0, 0
        res = list()
        while i_1<len_1 and i_2<len_2:
            if nums1[i_1]<=nums2[i_2]:
                res.append(nums1[i_1])
                i_1 += 1
            else:
                res.append(nums2[i_2])
                i_2 += 1
        res.extend(nums1[i_1:] if i_1<len_1 else nums2[i_2:])
        return res
        
    def sortArray_Radix(self, nums: List[int]) -> List[int]:
        head = ListNode(None)
        node = head
        max_val = min_val = nums[0]
        for num in nums:
            if num > max_val:
                max_val = num
            if min_val > num:
                min_val = num
            node.next = ListNode(num)
            node = node.next
        if min_val<0:
            val = max(max_val, abs(min_val))
        else:
            val = max_val
        key_count = len(str(val))
        for i in range(key_count):
            head = self.collect(self.distribute(head, i))
        
        return self.traverse(head)
        
    def distribute(self, head, key):
        lists = list()
        for _ in range(10):
            dummy_head = ListNode(None)
            node = dummy_head
            lists.append((dummy_head, node))
        node = head.next
        while node:
            val = node.val//(10**key)%10
            h, n = lists[val]
            n.next = node
            node = node.next
            n = n.next
            n.next = None
            lists[val] = (h, n)
        return lists

    def collect(self, lists):
        head, node = lists[0]
        for i in range(1, 10):
            h, n = lists[i]
            if not h==n:
                node.next = h.next
                node = n
        return head
    
    def traverse(self, head):
        node = head.next
        res = list()
        while node:
            res.append(node.val)
            node = node.next
        return res