class ind:
    def __init__(self):
        self.n=int(input())
        self.val=[int(i) for i in input().split()]
        le=len(self.val)
        if(le==self.n):
            for i in range(0,le):
                print(self.val[i],i)
o=ind()
    
