no=int(input())
l=[]
if no>1:
    for i in range(1,no+1):
        if((no%i)==0):
            l.append(i)
print(sep=" ",*l)
