import sys
input = sys.stdin.readline

N = int(input())
price = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    max_val = 0
    for j in range(1, i + 1):
        max_val = max(max_val, dp[i - j] + price[j])
    dp[i] = max_val

print(dp[N])