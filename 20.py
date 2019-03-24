a2=list(map(int,input().split()))
b2=sorted(list(map(int,input().split())))[::-1]
n2=0
for i in range(len(b2)):
  if(a2[1]>=b2[i]):
    n2+=int(a2[1]/b2[i])
    a2[1]%=b2[i]
if(a2[1]==0):
  print(n2)
else:
  print("it's not possible to select coins in such a way that they sum upto S")
