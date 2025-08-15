from collections import deque

dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(I, start_x, start_y, end_x, end_y):
    visited = [[False] * I for _ in range(I)]
    q = deque()
    q.append((start_x, start_y, 0))
    visited[start_x][start_y] = True

    while q:
        x, y, count = q.popleft()
        if x == end_x and y == end_y:
            return count
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, count + 1))

T = int(input())
for _ in range(T):
    I = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    print(bfs(I, start_x, start_y, end_x, end_y))
