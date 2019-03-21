class nk:
    def __init__(self):
        self.values=[int(i) for i in input().split()]
        self.n=self.values[0]
        self.k=self.values[1]
        self.sum=0
        self.lis=[int(i) for i in input().split()]           
    def fin(self):
        for i in range(0,self.k):
            self.sum+=self.lis[i]
        print(self.sum)
o=nk()
o.fin()
