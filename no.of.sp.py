class sp:
    def __init__(self):
        self.s=str(input())
        l=len(self.s)
        c=0
        for i in range(0,l):
            if(self.s[i].isalpha()==False)and(self.s[i].isdigit()==False):
                c+=1
        print(c)
o=sp()
