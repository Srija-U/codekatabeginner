class nu:
    def __init__(self):
        self.s=str(input())
        l=len(self.s)
        c=0
        for i in range(0,l):
            if(self.s[i].isdigit()==True):
                c+=1
        print(c)
o=nu()
