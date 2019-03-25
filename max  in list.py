class ma:
    def __init__(self):
        self.n=int(input())
        self.lis=[int(i) for i in input().split()]
    def maxi(self):
        if(self.n==len(self.lis)):
            a=max(self.lis)
            print(a)
o=ma()
o.maxi()
