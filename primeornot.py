class pri:
    def __init__(self):
        self.a=int(input())
    def fin(self):
        if(self.a>1):
            for i in range(2,self.a):
                if(self.a%i==0):
                    print("no")
                    break
            else:
                print("yes")
        else:
            print("no")
o=pri()
o.fin()
