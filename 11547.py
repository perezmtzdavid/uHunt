T = int(input())
vals = []

for i in range(T):
    vals.append(int(input()))

for i in vals:
    h = i*567
    h /= 9
    h += 7492
    h *= 235
    h /=47
    h -= 298
    print(str(int(h))[-2])