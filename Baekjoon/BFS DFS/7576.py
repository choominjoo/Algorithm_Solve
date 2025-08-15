from collections import deque

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j))
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if board[nx][ny] != 0:
            continue
        board[nx][ny] = board[x][y] + 1
        q.append((nx, ny))
ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(-1)
            exit(0)
        ans = max(ans, board[i][j])
print(ans - 1)