N1=int(input())
S1=str(N1)
c1=0
for i in range(0,len(S1)):
    if int(S1[i:i+2])<26 and len(str(int(S1[i:i+2])))==2:
        c1=c1+1
if c1==2:
    print(c1+c1//2)
else:
    print(c1+c1//2+1)
