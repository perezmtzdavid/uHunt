T = int(input())
count = 1

for i in range(T):
    a,b,c = map(int,input().split())
    if a <= 20 and b <= 20 and c <= 20:
        print("Case %d: good"%count)
    else:
        print("Case %d: bad"%count)
    count += 1