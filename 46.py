n2=int(input())
l1=list(map(int,input().split()))
a_has1=0
b_has1=0
l1.sort(reverse=True)
for i in l1:
  s=a_has1+i
  if b_has1>s:
    a_has1=s
  else:
    a_has1=b_has1
    b_has1=s
print(a_has1,b_has1)
