# 4분 소요
data = input()
split_point = len(data) // 2
left = data[:split_point]
right = data[split_point:]
left_sum = 0
right_sum = 0
for i in left: left_sum += int(i)
for j in right: right_sum += int(j)


if left_sum == right_sum:
    print("LUCKY")
else: print("READY")