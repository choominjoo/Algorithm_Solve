from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()
q.append((0, 0))
visited[0][0] = True
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if visited[nx][ny] or board[nx][ny] == 0:
            continue
        visited[nx][ny] = True
        board[nx][ny] = board[x][y] + 1
        q.append((nx, ny))
print(board[n - 1][m - 1])