class arm:
    def __init__(self):
        self.a=[int(i) for i in input().split()]
        self.b=[]
        for i in range(self.a[0]+1,self.a[1]):
            self.sum=0
            self.temp=i
            while(i>0):
                self.digit=i%10
                self.sum+=self.digit ** 3
                i//=10
            if(self.temp==self.sum):
                self.b.append(self.temp)
        print(*self.b,sep=' ')
o=arm()
        
