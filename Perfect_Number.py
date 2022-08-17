n=int(input())
b=0
for i in range (1,n):
    if n%i==0:
        b+=i
if n==b:
    print(True)
else:
    print(False)