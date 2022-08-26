n=int(input())
b=0
for i in range(1,n):
    if (i*(i+1))==n:
        b+=1
if b==1:
    print('YES')
else:
    print('NO')