T = int(input())
count = 1

for i in range(T):
    clowns = list(map(int,input().split()))
    clowns = clowns[1:]
    clowns.sort()
    print("Case %d: %d"%(count,clowns[-1]))
    count += 1

