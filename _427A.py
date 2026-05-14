t = int(input())
a = list(map(int, input().split()))

recruits = 0
untreated_crime = 0

for event in a:
    if event > 0:
        recruits += event
    else:
        if recruits > 0:
            recruits -= 1
        else:
            untreated_crime += 1

print(untreated_crime)
