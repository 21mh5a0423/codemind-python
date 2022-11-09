n=int(input())
x=list(map(int,input().split()))
s=0
c=0
a=0
m=0
for i in x:
    c+=1
    s+=i
a=s//c
for i in x:
    if i==a:
        m+=1
        break
if m>0:
    print("True")
else:
    print("False")
