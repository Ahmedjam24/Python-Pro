def  main():
	u1=0
	v1=[]
	n1=int(input())
	for i1 in range(n1):
		v1.append(int(input()))
	sub=n1//2
	for i1 in range(sub):
		s+=l[i]
	sub1=s/sub
	s=0
	for i1 in range(sub,n1):
		s+=l[i1]
	sub2=s/(n-sub)
	print(sub1,sub2)
	if sub1==sub2 :
		print('yes')
	else :
		print('no')
      
try:
  main()
except:
  print('invalid')
