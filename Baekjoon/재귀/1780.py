import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

count = {-1: 0, 0: 0, 1: 0}

def is_same(x, y, n):
    first = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != first:
                return False
    return True

def solve(x, y, n):
    if is_same(x, y, n):
        count[paper[x][y]] += 1
        return
    size = n // 3
    for dx in range(3):
        for dy in range(3):
            solve(x + dx * size, y + dy * size, size)

solve(0, 0, N)

print(count[-1])
print(count[0])
print(count[1])