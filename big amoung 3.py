class thr:
    def __init__(self):
        values=[int(i)for i in input().split()]
        self.a=values[0]
        self.b=values[1]
        self.c=values[2]
    def fin(self):
        if(self.a>self.b)and(self.a>self.c):
            print(self.a)
        elif(self.b>self.a)and(self.b>self.c):
            print(self.b)
        else:
            print(self.c)
d=thr()
d.fin()
