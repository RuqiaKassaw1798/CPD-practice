x1, x2, x3 = sorted(map(int, input().split()))
meeting_point = x2
total_minimum_distance = abs(x1 - meeting_point) + abs(x3 - meeting_point)
print(total_minimum_distance)
