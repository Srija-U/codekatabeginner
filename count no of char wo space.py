class ch:
    def __init__(self):
        self.s=str(input())
        l=len(self.s)
        c=0
        for i in range(0,l-1):
            if(self.s[i]==' '):
                c=c+1
        l-=c
        print(l)
o=ch()
