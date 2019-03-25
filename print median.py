import math
class med:
    def __init__(self):
        self.n=int(input())
        self.lis=[int(i) for i in input().split()]
        self.lis.sort()
    def fin(self):
        l=math.ceil(self.n/2)
        print(self.lis[l-1])
o=med()
o.fin()
