location = input()
step = [(2, 1), (2,-1), (-2,1), (-2, -1), (1,2), (-1,2), (1, -2), (-1,-2)]
count = 0

x = ord(location[0]) - ord('a') + 1  # a=1, b=2, ..., h=8
y = int(location[1])

# 풀이 1
# for i in range(len(step)):
#     dx = x + step[i][0]
#     dy = y + step[i][1]
#     if dx <= 8 and dx >= 1 and dy <= 8 and dy >= 1:
#         count += 1

# print(count)

# 풀이 2
for i in step:
    dx = x + i[0]
    dy = y + i[1]
    if 1 <= dx <= 8 and 1 <= dy <= 8:
        count += 1

print(count)
