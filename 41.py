a1,b1=input().split()
a1=int(a1)
b1=int(b1)
s1=''
u=2
if(a1+b1<=3):
    for i in range(0,a1+b1):
        if(i%2!=0):
            s1=s1+'0'
        else:
            s1=s1+'1'
else:    
    for i in range(0,a1+b1):
        if(i==u):
            s1=s1+'0'
            if(u==b):
                u=u+2
            else:
                u=u+3
        else:
            s1=s1+'1'
y1=len(s1)-1
if(int(s1[y1])==0):
    print('-1')
elif a1==1 and b1==2: print("011")
else:
    print(s1)
