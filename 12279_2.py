T = int(input())
count = 1
res = 0

while True:
    if T == 0:
        break
    cases = list(map(int,input().split()))
    for i in cases:            
        if i > 0 and i < 100:                
            res += 1
        else:
            res -= 1
    print("Case %d: %d"%(count,res))
    count += 1
    res = 0 
    T = int(input())