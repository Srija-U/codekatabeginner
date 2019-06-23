n=str(input())
l=len(n)
c=0
for i in range(0,l):
    if(n[i].isnumeric()):
        c=c+1
print(c)
