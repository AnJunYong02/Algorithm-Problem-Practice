arr = list(map(int, input()))

# 1. 0이 아니면 모두 곱하기
# 2. 0이면 더하기
result = arr[0]

for i in range(1, len(arr)):
    if arr[i-1] == 0 or arr[i-1] == 1:
        result = int(arr[i-1]) +  int(arr[i])
    else:
        result = result * int(arr[i])

print(result)