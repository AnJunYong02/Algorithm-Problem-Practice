# 80분 소요
from collections import Counter

data = list(input())
data.sort()

output = ""
count = Counter(data) # 각 문자 등장 갯수 세기
odd_count = 0
odd_char = ''

for word in count:
    if count[word] % 2 == 1: # 문자가 홀수개라면 -> 하나 중간에 넣어야 함.
        odd_count += 1
        odd_char = word
        if odd_count == 2:
            print("I'm Sorry Hansoo")
            exit(0)

for i in range(0, len(data), 2):
    if count[data[i]] % 2 == 1:
        count[data[i]] -= 1
    else:
        output += data[i]

tmp = output[::-1] # 뒤집기
output += odd_char
output += tmp
print(output)