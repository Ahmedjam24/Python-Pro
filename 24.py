a2=int(input())
d2,m2=[],[]
for i in range(0,2**a2):
  b='{:2b}'.format(i)
  if len(b)<a2:
    c='0'*(a2-len(b))+b
    d2.append(c)
  else:
    d2.append(b[-a2:])
for i in range(0,len(d2)):
  p1=list(d2[i])
  if ' ' in p1:
    k=p1.index(' ')
    p1[k]='0'
  m2.append(''.join(p1))
for i in m2:
  print(i)
