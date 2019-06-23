l=[int(i) for i in input().split()]
n=l[0]
k=l[1]
l=[int(i) for i in input().split()]
c=0
for i in l:
    if(i==k):
        c=c+1
print(c)
