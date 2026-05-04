s = input().replace("{", "").replace("}", "").replace(",", "")
distinct_letters = set(s.split())
print(len(distinct_letters))
