n=int(input())
p, *a=list(map(int,input().split()))
q, *b=list(map(int,input().split()))

c=set(a+b)
if len(c)==n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
