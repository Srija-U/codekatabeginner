l=[str(i) for i in input().split()]
s=l[0]
n=int(l[1])
t=len(s)
te=t-n
for i in range(te,t):
    print(s[i],end="")
