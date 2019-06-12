n1,m1=map(int,input().split())
e1=[]
for i in range(m1):
  e1.append(list(map(int,input().split())))
cost=10000000
f=0
for i in range(m1):
  if e1[i][0]==1:
    s=e1[i][1]
    c=e1[i][2]
    for j in range(i+1,m1):
      if e1[j][0]==s:
        s=e1[j][1]
        c+=e1[j][2]
    if c<cost and s==n1:
      cost=c
      f+=1
if f==0:
  print(-1)
else:
  print(cost)
