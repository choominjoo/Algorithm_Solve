def func(A, B, C):
    if B == 1:
        return A % C

    num = func(A, B // 2, C)
    if B % 2 == 0:
        return (num * num) % C
    else:
        return (num * num * A) % C
    
A, B, C = map(int, input().split())
print(func(A, B, C))