class fib:
    def __init__(self):
        self.n=int(input())
        self.lis=[]
        s=0
        for i in range(0,self.n):
            if(i==0):
                self.lis.append('1')
            elif(i==1):
                self.lis.append('1')
            else:
                s=int(self.lis[i-2])
                s+=int(self.lis[i-1])
                self.lis.append(s)
        print(*self.lis,sep=' ')
o=fib()
            
                
