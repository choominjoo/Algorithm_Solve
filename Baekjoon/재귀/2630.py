import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

def is_same(x, y, n):
    first = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != first:
                return False
    return True

def solve(x, y, n):
    global white, blue
    if is_same(x, y, n):
        if paper[x][y] == 0:
            white += 1
        else:
            blue += 1
        return
    size = n // 2
    solve(x, y, size)
    solve(x + size, y, size)
    solve(x, y + size, size)
    solve(x + size, y + size, size)

solve(0, 0, N)
print(white)
print(blue)