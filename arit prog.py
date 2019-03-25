class ap:
    def __init__(self):
        self.values=[int(i) for i in input().split()]
        self.n=self.values[0]
        self.a=self.values[1]
        self.d=self.values[2]
        self.sum=0
        for i in range(0,self.n):
            self.sum+=self.a
            self.a=self.a+self.d
        print(self.sum)
ob=ap()
