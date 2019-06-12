n1=int(input())
l1=list(map(int,input().split()))
t1=[]
c1=1
for i in range(n1):
	for j in range(i,n1):
		if j==n1-1:
			break
		if (l1[j]>0 and l1[j+1]<0) or (l1[j]<0 and l1[j+1]>0):
			c1=c1+1
		else:
			break
	t1.append(c1)
	c1=1
print(*t1)
