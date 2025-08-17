import sys
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

def binary_search(arr, target):
    st, en = 0, len(arr) - 1
    while st <= en:
        mid = (st + en) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            st = mid + 1
        else:
            en = mid - 1
    return 0

for x in targets:
    print(binary_search(a, x))