s=str(input())
a=0
n=0
l=len(s)
for i in range(0,l):
    if(s[i].isalpha()):
        a=a+1
    if(s[i].isnumeric()):
        n=n+1
if((a==0)or(n==0)):
    print("No")
else:
    print("Yes")
