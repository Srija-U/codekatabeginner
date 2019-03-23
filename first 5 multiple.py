class mul:
    def __init__(self):
        self.a=int(input())
        self.b=[]
        for i in range(1,6):
            self.b.append(i*self.a)
        print(*self.b,sep=' ')
o=mul()
