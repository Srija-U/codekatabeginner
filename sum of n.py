class su:
    def __init__(self):
        self.a=int(input())
        self.sum=0
    def fin(self):
        for i in range(1,self.a+1):
            self.sum=self.sum+i
        print(self.sum)
o=su()
o.fin()
