li=[int(i) for i in input().split()]
l=li[0]
b=li[1]
h=li[2]
tsa=2*((l*b)+(b*h)+(l*h))
vol=l*b*h
print(tsa,vol)
