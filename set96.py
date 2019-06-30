s=str(input())
s=s.lower()
l=[]
for i in s:
    if(i in l):
        print("No")
        exit()
    else:
        l.append(i)
print("Yes")
