no=int(input())
if no>1:
    for i in range(2,no):
        if((no%i)==0):
            print("yes")
            break
    else:
        print("no")
