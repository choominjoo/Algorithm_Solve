n, m = map(int, input().split())
result = []

def backtrack(depth):
    if depth == m:
        print(*result)
        return
    for i in range(1, n + 1):
        result.append(i)
        backtrack(depth + 1)
        result.pop()

backtrack(0)