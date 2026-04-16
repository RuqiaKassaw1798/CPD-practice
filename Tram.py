n=int(input())
x=0
capacity=0
for i in range(n):
    a,b=map(int,input().split())
    x-=a
    x+=b
    capacity=max(capacity,x)
print(capacity)
