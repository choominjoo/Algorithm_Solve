n = int(input())
s = [0] + [int(input()) for _ in range(n)]
tot = sum(s)
if n <= 2:
    print(tot)
else:
    d = [0] * (n + 1)
    d[1] = s[1]
    d[2] = s[2]
    d[3] = s[3]
    for i in range(4, n):
        d[i] = min(d[i - 2], d[i - 3] + s[i])
    print(tot - min(d[n - 1], d[n - 2]))