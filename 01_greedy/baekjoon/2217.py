# 30분 소요
N = int(input())
data = [int(input()) for _ in range(N)]
data.sort()

result = 0
for i in range(N):
    tmp  = data[i] * (N - i)
    if tmp > result:
        result = tmp

print(result)