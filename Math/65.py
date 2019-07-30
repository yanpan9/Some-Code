class Solution:
    def __init__(self):
        self.c2i = {
            " ":0,
            "+":1,
            "-":1,
            ".":3,
            "e":4
        }
        for i in range(10):
            self.c2i[str(i)]=2
        self.transfer = [
            [0,1,6,2,-1],
            [-1,-1,6,2,-1],
            [-1,-1,3,-1,-1],
            [8,-1,3,-1,4],
            [-1,7,5,-1,-1],
            [8,-1,5,-1,-1],
            [8,-1,6,3,4],
            [-1,-1,5,-1,-1],
            [8,-1,-1,-1,-1]
        ]
        
    def isNumber(self, s: str) -> bool:
        state = 0
        finals = 0b101101000
        for c in s:
            idx = self.c2i.get(c, -1)
            if idx == -1: return False
            state = self.transfer[state][idx]
            if state == -1: return False
        return (finals&(1<<state))>0