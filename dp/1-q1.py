
n, x, y = map(int, input().split(' '))

for _ in range(n-2):
    a_i = (x + y) % 100
    x = y
    y = a_i

print(y)