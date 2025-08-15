from collections import deque

n, k = map(int, input().split())
MAX = 100001
dist = [-1] * MAX
q = deque()
q.append(n)
dist[n] = 0
while q:
    cur = q.popleft()
    if cur == k:
        print(dist[cur])
        break
    for nx in (cur - 1, cur + 1, cur * 2):
        if 0 <= nx < MAX and dist[nx] == -1:
            dist[nx] = dist[cur] + 1
            q.append(nx)