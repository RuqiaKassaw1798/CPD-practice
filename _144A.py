n = int(input())
a = list(map(int, input().split()))
max_pos = a.index(max(a))
min_pos = len(a) - 1 - a[::-1].index(min(a))
swaps = max_pos + (n - 1 - min_pos)
if max_pos > min_pos:
    swaps -= 1
print(swaps)
