n=int(input())
l=[int(i) for i in input().split()]
for i in range(1,len(l)-1):
    if(l[i-1]>l[i])or(l[i]>l[i+1]):
        print(l.index(l[i]))
        break
