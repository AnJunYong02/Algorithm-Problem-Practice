# 4분 소요
S = input()
num_arr = []
str_arr = []
sum = 0
for ch in S:
    if ch.isalpha(): # 문자열이면
        str_arr.append(ch)
    else: sum += int(ch)
str_arr.sort()

if sum != 0: str_arr.append(str(sum))
print("".join(str_arr))