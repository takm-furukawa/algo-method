n = int(input())

patterns = [1] + [0 for _ in range(n)]

for i in range(1, n + 1):
    if i == 1:
        patterns[i] = 1
        continue
    
    patterns[i] = patterns[i-1] + patterns[i-2]

print(patterns[-1])