l=[int(i) for i in input().split()]
n=l[0]
s=l[1]
l=[int(i) for i in input().split()]
f=0
for i in range(0,n):
    if(l[i]%2==1):
        f=f+1
    if(f==s):
        print(l[i])
        break
