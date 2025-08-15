def lotto(start, depth):
    if depth == 6:
        print(*selected)
        return
    for i in range(start, len(s)):
        selected.append(s[i])
        lotto(i + 1, depth + 1)
        selected.pop()

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    s = nums[1:]
    selected = []
    lotto(0, 0)
    print()