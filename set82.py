s=str(input())
l=len(s)
f=0
for i in range(0,l):
    if(s[i]=='a')or(s[i]=='e')or(s[i]=='i')or(s[i]=='o')or(s[i]=='u')or(s[i]=='A')or(s[i]=='E')or(s[i]=='I')or(s[i]=='O')or(s[i]=='U'):
        f=1
        break
    else:
        f=0
if(f==0):
    print("no")
else:
    print("yes")
