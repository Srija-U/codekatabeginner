class od:
    def __init__(self):
        self.a=[int(i) for i in input().split()]
        self.b=[]
        for i in range(self.a[0]+1,self.a[1]):
            if(i%2==1):
                self.b.append(i)
        print(*self.b, sep =' ')
o=od()
