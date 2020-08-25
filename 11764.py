T = int(input())
res = []
for i in range(T):
    N = int(input())
    h_jump = 0
    l_jump = 0
    h_walls = 0     
    walls = input().split()
    walls = list(map(int,walls))
    for j in range(N-1):
        if N < 2:            
            res.append([0,0])
            break
        if walls[j] > walls[j+1]:
            l_jump += 1                        
        elif walls[j] < walls[j+1]:
            h_jump += 1                        
    res.append([h_jump,l_jump])    

for i in range(T):
    print("Case %d: %d %d" % (i+1,res[i][0],res[i][1]))
