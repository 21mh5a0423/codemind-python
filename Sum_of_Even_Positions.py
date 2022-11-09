n=int(input())
x=list(map(int,input().split()))
c=0
for i in range(len(x)):
    if i%2==0:
        c+=x[i]
print(c)