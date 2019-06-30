import math
l=[int(i) for i in input().split()]
p=l[0]*l[1]
r=math.sqrt(p)
if(r-math.floor(r)==0):
    print("yes")
else:
    print("no")
