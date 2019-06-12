n2,p1,q1,r1=map(int,input().split())
a1=[int(i) for i in input().split()]
c1=[p1*a1[i]+q1*a1[j]+r1*a1[k] for i in range(len(a1)) for j in range(len(a1)) for k in range(len(a1)) if i<=j<=k]
print(max(c1))
