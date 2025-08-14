def func(n, r, c):
	if n == 0:
		return 0
		
	num = 2 ** (n - 1)
	if r < num and c < num:
		return func(n - 1, r, c)
	if r < num and c >= num:
		return num * num + func(n - 1, r, c - num)
	if r >= num and c < num:
		return 2 * num * num + func(n - 1, r - num, c)
	return 3 * num * num + func(n - 1, r - num, c - num)
	
n, r, c = map(int, input().split())
print(func(n, r, c))