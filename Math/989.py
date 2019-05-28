class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        len_a = len(A)
        B = list()
        while K:
            K, val = divmod(K, 10)
            B.insert(0, val)
        len_b = len(B)
        if len_a != len_b:
            if len_a - len_b > 0 :
                B = [0]*(len_a-len_b)+B
            else:
                A = [0]*(len_b-len_a)+A
        count = 0
        for i in range(max(len_a, len_b)-1, -1, -1):
            sum_val = A[i]+B[i]+count
            count, A[i] = divmod(sum_val, 10)
        if count:
            A.insert(0, count)
        return A