n, m = map(int, input().split())
result = []

def backtrack(start, depth):
    if depth == m:
        print(*result)
        return
    for i in range(start, n + 1):
        result.append(i)
        backtrack(i, depth + 1)
        result.pop()

backtrack(1, 0)