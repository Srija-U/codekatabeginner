class arm:
    def __init__(self):
        self.a=int(input())
        self.sum=0
        self.temp=self.a
        while(self.a>0):
            self.digit=self.a%10
            self.sum+=self.digit ** 3
            self.a//=10
        if(self.temp==self.sum):
            print("yes")
        else:
            print("no")
o=arm()
        
