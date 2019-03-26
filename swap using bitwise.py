class sw:
    def __init__(self):
        self.val=[int(i) for i in input().split()]
        self.val[0],self.val[1]=(self.val[0]^self.val[1])^((self.val[0]^self.val[1])^self.val[1]),(self.val[0]^self.val[1])^self.val[1]
        print(*self.val,sep=' ')
o=sw()

