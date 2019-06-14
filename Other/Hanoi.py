# -*- coding:utf-8 -*-

class Hanoi:
    def __init__(self):
        self.result = list()
    def getSolution(self, n, src="left", cache="mid", dst="right"):
        if n == 1:
            self.result.append("move from %s to %s"%(src, dst))
        else:
            self.getSolution(n-1, src=src, cache=dst, dst=cache)
            self.getSolution(1, src=src, cache=cache, dst=dst)
            self.getSolution(n-1, src=cache, cache=src, dst=dst)
        return self.result