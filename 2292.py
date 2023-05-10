# baekjoon-python
learn baekjoon python by my self.(백준 독학 저장소)

#은 수식 설명

# 벌집의 규칙은 방을 1개 거쳐야 하는 숫자는 1개, 2개 거쳐야 하는 숫자는 6개, 3개 거쳐야 하는 숫자는 12개, 4개 거쳐야 하는 숫자는 18개, 5개 거쳐야 하는 숫자는 24개....
n = int(input())
a = 1                    # 지나갈 방의 갯수
b = 6                    # 주어진 규칙으로 거처야할 방의 갯수가 늘어날 때마다 방의 갯수가 6개씩 늘어남
c = 1                    # 최초의 방
while n > c:             
  a += 1                 # 방의 갯수가 늘어남
  c += b                 # 방의 갯수를 더함
  b += 6                 # 6개씩 늘어나게 설정
print(a)
