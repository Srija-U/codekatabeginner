s=str(input())
l=len(s)
for i in range(0,l):
    if(s[i]=='/'):
        p=s.index(s[i])
        a=int(s[0:p])
        b=int(s[p+1:l])
        print(int(a/b))
    if(s[i]=='%'):
        p=s.index(s[i])
        a=int(s[0:p])
        b=int(s[p+1:l])
        print(int(a%b))
