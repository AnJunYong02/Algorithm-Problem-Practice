n = int(input())
arr = list(map(int, input().split()))
# 1 2 3 3 => 2
# 2 3 1 2 2 => 1 2 2 2 3
# 1 1 1 4 => 3그룹
arr.sort()
count = 0 # 그룹 안에 있는 사람
result = 0 # 그룹 수


for i in range(n):
    count += 1
    if count >= arr[i]:
        result += 1
        count = 0

print(result)