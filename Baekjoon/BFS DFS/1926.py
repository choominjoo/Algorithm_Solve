from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
num = 0
size = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] or board[i][j] == 0:
            continue
        num += 1
        q = deque()
        visited[i][j] = True
        q.append((i, j))
        temp = 1
        while q:
            x, y = q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if visited[nx][ny] or board[nx][ny] == 0:
                    continue
                visited[nx][ny] = True
                q.append((nx, ny))
                temp += 1
        size = max(size, temp)
print(num)
print(size)