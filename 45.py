n2=input()
c1=1
if n2==n2[::-1]:
    print("yes")
else:
    x=n2.strip("0")
    if x==x[::-1]:
        print("yes")
    else:
        print("no")
