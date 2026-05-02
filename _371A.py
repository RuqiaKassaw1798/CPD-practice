n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(k):
    group = a[i::k]
    c1 = group.count(1)
    c2 = len(group) - c1
    ans += min(c1, c2)

print(ans)
