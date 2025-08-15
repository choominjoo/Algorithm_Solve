n = int(input())
r = [0] * (n + 1)
g = [0] * (n + 1)
b = [0] * (n + 1)
for i in range(1, n + 1):
    r[i], g[i], b[i] = map(int, input().split())
d = [[0] * 3 for _ in range(n + 1)]
d[1][0] = r[1]
d[1][1] = g[1]
d[1][2] = b[1]
for i in range(2, n + 1):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + r[i]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + g[i]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + b[i]
print(min(d[n]))