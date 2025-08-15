n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def func(cur, total):
	global cnt
	if cur == n:
		if total == s:
			cnt += 1
		return
	func(cur + 1, total + arr[cur])
	func(cur + 1, total)

func(0, 0)
if s == 0:
	cnt -= 1
print(cnt)