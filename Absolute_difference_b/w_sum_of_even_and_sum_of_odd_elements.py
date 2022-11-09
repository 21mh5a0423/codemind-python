n=int(input())
x=list(map(int,input().split()))
e=0
o=0
for i in x:
    if i%2==0:
        e+=i
    else:
        o+=i
print(abs(e-o))