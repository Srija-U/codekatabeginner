l=str(input())
c=0
for i in range(0,len(l)):
    if((l[i]=='0')or(l[i]=='1')):
        c=c+1
    else:
        c=0
        print("no")
        exit()
if(c==0):
    print("no")
else:
    print("yes")
