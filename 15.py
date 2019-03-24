
n1 = int(input())
in_num = list(map(int, input().split()))
 
no_of_one = []
for i in in_num:
    count = 0
    while i:
        i &= (i-1)
        count += 1
    no_of_one.append(count)
 
result = sorted(zip(no_of_one, in_num), reverse=True)
print(*[num for _, num in result], sep='\n')
