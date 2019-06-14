l1=[int(i) for i in input().split()]
l2=[int(i) for i in input().split()]
l3=[]
l3.append(abs(l1[0]-l2[0]))
l3.append(abs(l1[1]-l2[1]))
print(sep=" ",*l3)
