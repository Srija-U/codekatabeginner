class ti:
    def __init__(self):
        self.i=int(input())
        self.lis=[0,0]
        if(self.i<=59):
            self.lis[1]=self.i
        else:
            r=self.i//60
            self.i-=(60*r)
            self.lis[0]=r
            self.lis[1]=self.i
        print(*self.lis,sep=' ')
o=ti()
