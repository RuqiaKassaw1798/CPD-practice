n=int(input())
bills=[100,20,10,5,1]
c=0
for b in bills:
    c+=n//b
    n%=b
print(c)
