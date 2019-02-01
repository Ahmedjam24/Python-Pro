usr=raw_input()
usr1=raw_input()
length=len(usr)
if(len(usr1)<len(usr)):
    length=len(usr1)
str=""
for i in range(length):
    if(usr[i]==usr1[i]):
        str=str+usr[i]
    else:
        break;
print str
