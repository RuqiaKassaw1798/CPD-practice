for i in range(5):
    a=list(map(int,input().split()))
    if 1 in a:
        print(abs(i-2)+abs(a.index(1)-2))
