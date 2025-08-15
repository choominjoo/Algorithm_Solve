N = int(input())
times = list(map(int, input().split()))

times.sort()

total = 0
sum = 0

for time in times:
    sum += time
    total += sum

print(total)