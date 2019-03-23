class pal:
    def __init__(self):
        self.a=str(input())
        self.b=self.a[::-1]
        if(self.a==self.b):
            print("yes")
        else:
            print("no")
o=pal()
