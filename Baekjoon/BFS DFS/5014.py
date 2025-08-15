from collections import deque

def bfs(F, S, G, U, D):
    visited = [False] * (F + 1)
    q = deque()
    q.append((S, 0))
    visited[S] = True

    while q:
        current, count = q.popleft()
        if current == G:
            return count
        for next_floor in (current + U, current - D):
            if 1 <= next_floor <= F and not visited[next_floor]:
                visited[next_floor] = True
                q.append((next_floor, count + 1))
    return "use the stairs"

F, S, G, U, D = map(int, input().split())
print(bfs(F, S, G, U, D))