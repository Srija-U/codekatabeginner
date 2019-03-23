class po:
    def __init__(self):
        self.a=[int(i) for i in input().split()]
        self.b=pow(self.a[0],self.a[1])
        print(self.b)
o=po()
