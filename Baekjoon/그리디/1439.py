S = input()

count0 = 0
count1 = 0

if S[0] == '0':
    count0 += 1
else:
    count1 += 1

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        if S[i] == '0':
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))