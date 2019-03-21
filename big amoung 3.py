class thr:
    def __init__(self):
        self.a=int(input())
        self.b=int(input())
        self.c=int(input())
    def fin(self):
        if(self.a>self.b)and(self.a>self.c):
            print(self.a)
        elif(self.b>self.a)and(self.b>self.c):
            print(self.b)
        else:
            print(self.c)
d=thr()
d.fin()
