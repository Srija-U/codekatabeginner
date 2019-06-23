n=int(input())
l=[int(i) for i in input().split()]
l.sort()
print(l[0],end=" ")
print(l[n-1])
