N, M = map(int, input().split())
data = list(map(int, input().split()))

count = 0
result_dict = dict()

for i in range(N-1):
    standard = data[i]
    for j in range(i + 1, N):
        if standard == data[j]:
            continue
        else:  # 숫자가 다르다면 {1:2}, {1:3}
            result_dict[i+1] = j+1
            count += 1

print(count)    