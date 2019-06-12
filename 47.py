n2,k1=map(int,input().split())
if n2%10==0:
  n2=str(n2)
  c=0
  for i in range(len(n2)-1,-1,-1):
    if n2[i]=='0':
      c+=1
  if k1<=c:
    print(n2)
  else:
    n2=n2[:-c]
    n2=n2+'0'*k1
    print(n2)
elif 10%(n2%10)==0:
  no=int('1'+'0'*k1)
  while True:
    if no%n2==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*k1)
else:
  print(str(n2)+k1*'0')
