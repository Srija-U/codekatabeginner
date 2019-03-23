class pri:
    def __init__(self):
        self.a=[int(i) for i in input().split()]
        self.b=[]
    def fin(self):
        for i in range(self.a[0]+1,self.a[1]-1):
            if(i>1):
                for j in range(2,i):
                    if(i%j==0):
                        break
                else:
                    self.b.append(i)
            else:
                next
        print(*self.b,sep=' ')
o=pri()
o.fin()
