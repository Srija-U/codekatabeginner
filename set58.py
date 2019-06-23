n=int(input())
l=[int(i) for i in input().split()]
s=0
le=len(l)
for i in l:
    s=s+i
s=s/le
print(s)
