class fa:
    def __init__(self):
        self.a=int(input())
        self.prod=1
        for i in range(1,self.a+1):
            self.prod*=i
        print(self.prod)
o=fa()
            
