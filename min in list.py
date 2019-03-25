class mi:
    def __init__(self):
        self.n=int(input())
        self.lis=[int(i) for i in input().split()]
    def mini(self):
        if(self.n==len(self.lis)):
            a=min(self.lis)
            print(a)
o=mi()
o.mini()
