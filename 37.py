import sys,string
n2 = int(input())
L1 = [ int(x) for x in input().split()]
n1 = len(L1)
if n2==1 :
    print(1)
    sys.exit()
cnt = 0
for i in range(1,n2-1) :
    if ((L1[i] > L1[i-1]) and (L1[i] > L1[i+1])) or ((L1[i] < L1[i-1]) and (L1[i] < L1[i+1])):
        cnt += 1
print(cnt)
