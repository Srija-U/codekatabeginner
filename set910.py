s=str(input())
l=[]
for i in s:
    if (i.isnumeric()):
        l.append(i)
print(sep="",*l)
