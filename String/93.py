from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = list()
        length = len(s)
        self.dfs(list(), 0, s, length)
        return self.res
        
    def dfs(self, lst: List[str], count: int, s: str, length:int):
        if length==0:
            if count==4:
                self.res.append(".".join(lst))
        else:
            for i in range(min(3, length)):
                sub_str = s[:i+1]
                if length-i-1>(3-count)*3:
                    continue
                else:
                    num = int(sub_str)
                    if num>255:
                        continue
                    elif str(num)!=sub_str:
                        continue
                    else:
                        lst.append(sub_str)
                        self.dfs(lst, count+1, s[i+1:], length-i-1)
                        lst.pop()