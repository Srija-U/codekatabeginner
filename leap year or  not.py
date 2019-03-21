class ye:
    def __init__(self):
        self.a=int(input())
    def fin(self):
        if(self.a%4==0):
            if(self.a%100==0):
                if(self.a%400==0):
                    print("yes")
                else:
                    print("no")
            else:
                print("yes")
        else:
            print("no")
ob=ye()
ob.fin()
                    
