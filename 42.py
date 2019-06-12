num2,k=map(int,input().split())
l1=list(map(int,input().split()))
if k==1:
    print(min(l1))
elif k==2:
    print(max(l1[0],l1[num2-1]))
else:
    print(max(l1))
