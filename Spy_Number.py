n=int(input())
a=str(n)
s=0
p=1
d=0
for i in a:
    d=int(i)
    s+=d
    p*=d
if s==p:
    print('Spy Number')
else:
    print('Not Spy Number')
    