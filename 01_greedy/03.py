n = map(int, input())
data = list(map(int, input().split()))

result = 1
# 3 2 1 1 9 -> 1 1 2 3 9
data.sort()
sum = 0 # 동전들 합친 것들
for i in range(1, data[len(data)-1]):
    if sum <= i:
        sum += data[i]
        continue
    else:
        result = i
