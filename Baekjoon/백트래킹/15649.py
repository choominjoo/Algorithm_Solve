n, m = map(int, input().split())
arr = [0] * 10
isused = [False] * 10

def func(k):
	if k == m:
		print(*arr[:m])
		return
	for i in range(1, n + 1):
		if not isused[i]:
			arr[k] = i
			isused[i] = True
			func(k + 1)
			isused[i] = False

func(0)