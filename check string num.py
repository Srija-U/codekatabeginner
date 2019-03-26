class nu:
    def __init__(self):
        s=str(input())
        l=len(s)
        for i in range(0,len(s)-1):
            if(s[i]=='.'):
                s=s.replace(".","")
        if(s.isdigit()==True):
            print("yes")
        else:
            print("No")
o=nu()
