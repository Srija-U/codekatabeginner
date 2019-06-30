s=str(input())
s=s.lower()
l=[]
for i in s:
    if(i in l):
        print("no")
        exit()
    else:
        l.append(i)
print("yes")
