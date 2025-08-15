n = int(input())
cnt = 0
isused1 = [False] * n
isused2 = [False] * (2 * n - 1)
isused3 = [False] * (2 * n - 1)

def func(cur):
	global cnt
	if cur == n:
		cnt += 1
		return
	for i in range(n):
		if isused1[i] or isused2[i + cur] or isused3[cur - i + n - 1]:
			continue
		isused1[i] = isused2[i + cur] = isused3[cur - i + n - 1] = True
		func(cur + 1)
		isused1[i] = isused2[i + cur] = isused3[cur - i + n - 1] = False
		
func(0)
print(cnt)