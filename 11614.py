import math           

T = int(input())
vals = []

for i in range(T):
    vals.append(input())

vals = list(map(int,vals))

for i in vals:
    res = (-1 + int(math.sqrt(1+(8*i))))//2
    print(res)

