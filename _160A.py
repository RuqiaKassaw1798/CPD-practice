n=int(input())
a=sorted(map(int,input().split()),reverse=True)
s=t=0
for i,x in enumerate(a,1):
    s+=x
    if s>sum(a)-s:
        print(i)
        break
