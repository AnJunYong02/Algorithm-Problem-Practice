n, m = map(int, input().split())
x, y, direction = map(int, input().split())
d = [[0] * m for _ in range(n)]
d[x][y] = 1  # 현재 위치 방문 처리

# 맵 정보 입력 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

count = 1
dx = [0, 1, 0, -1]  # 북, 동, 남, 서
dy = [-1, 0, 1, 0]  # 북, 동, 남, 서

dx_back = [0, -1, 0, 1]  # 북, 동, 남, 서
dy_back = [1, 0, -1, 0]  # 북, 동, 남, 서

while True:
    direction = (direction - 1) % 4  # 왼쪽 방향으로 회전
    tmp_x = x + dx[direction]
    tmp_y = y + dy[direction]

    if d[tmp_x][tmp_y] == 0 and array[tmp_x][tmp_y] == 0: # 방문하지 않은 곳이라면 -> 한 칸 전진
        x += dx[d]
        y += dy[d]
        d[x][y] = 1  # 방문한 곳으로 표시
        count += 1  # 방문한 곳 카운트

    elif array[tmp_x][tmp_y] == 2 : # 이미 방문한 곳이라면 -> 왼쪽 방향으로 회전만 수행 함
        direction = (direction - 1) % 4

    else : # 바다라면 -> 뒤로 한칸 감 -> 물러났을 떄 바다일시 마무리
        x += dx_back[direction]
        y += dy_back[direction]
        if array[x][y] == 0:
            d[x][y] = 1  # 방문한 곳으로 표시
            count += 1
        elif array[x][y] == 1:  # 바다라면 -> 더 이상 진행할 수 없음
            break

print(count)

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1