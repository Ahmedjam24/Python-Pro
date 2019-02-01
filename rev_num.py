usr=int(raw_input())
check=usr
num=0
while(usr>0):
	rem=usr%10
	num=(num*10)+rem
	usr=usr/10
print num
