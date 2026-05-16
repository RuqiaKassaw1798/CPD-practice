s = input()
prev = 0

for c in s:
    curr = int(f"{ord(c):08b}"[::-1], 2)
    print((prev - curr) % 256)
    prev = curr
