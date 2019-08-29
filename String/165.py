class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]
        l1, l2 = len(v1), len(v2)
        i = 0
        while i<l1 and i<l2:
            if v1[i]>v2[i]:
                return 1
            elif v1[i]<v2[i]:
                return -1
            else:
                i += 1
        if i<l1:
            if sum(v1[i:]):
                return 1
            else:
                return 0
        elif i<l2:
            if sum(v2[i:]):
                return -1
            else:
                return 0
        else:
            return 0