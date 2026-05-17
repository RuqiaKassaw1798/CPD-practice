n = int(input())
scores = list(map(int, input().split()))

max_score = scores[0]
min_score = scores[0]
count = 0

for score in scores[1:]:
    if score > max_score:
        count += 1
        max_score = score
    elif score < min_score:
        count += 1
        min_score = score
      
print(count)
