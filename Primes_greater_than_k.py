def is_prime(z):
    y=0
    for i in range(1,z+1):
        if z%i==0:
            y+=1
    if y<=2:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
x=int(input())
c=0
for i in l:
    if i>=x:
        if is_prime(i):
            c+=1
print(c)