class mi:
    def __init__(self):
        self.n=int(input())
        self.lis=[int(i) for i in input().split()]
    def mini(self):
        if(self.n==len(self.lis)):
            self.lis.sort()
            print(*self.lis,sep=' ')
o=mi()
o.mini()
