import math
s=str(input())
sl=list(s)
l=len(s)
if(l%2==0):
    r=math.floor((l+1)/2)
    t=math.ceil((l+1)/2)
    sl[r-1]='*'
    sl[t-1]='*'
else:
    r=int((l+1)/2)
    sl[r-1]='*'
print(sep="",*sl)
