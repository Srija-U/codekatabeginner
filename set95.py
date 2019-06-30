s=str(input())
l1=[]
l2=[]
for i in range(0,len(s)):
    if(i%2==0):
        l1.append(s[i])
    else:
        l2.append(s[i])
print(sep='',*l1,end=" ")
print(sep='',*l2)
