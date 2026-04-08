n=int(input())
count=0
for i in range(n):
    a=list(map(int,input().split()))
    k=a.count(1)
    if k>=2:
        count+=1
print(count)
