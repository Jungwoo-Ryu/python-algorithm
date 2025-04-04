# for input

# multiple inputs by space
data = list(map(int, input().split()))
print(data)

a, b = map(int, input().split())
print(a, b)


import sys
# N, M = map(int, sys.stdin.readline().split())

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(board)

data = sys.stdin.readline().rstrip()
print(data)