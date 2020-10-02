def find_lr():
    temp_l,temp_r = 0,0    
    for i in range(l):        
        if soldiers[i] != 0:
            temp_l = soldiers[i]
    for i in range(r,s):
        if soldiers[i] != 0:
            temp_r = soldiers[i]
            break
    if temp_l == 0:
        temp_l = '*'
    if temp_r == 0:
        temp_r = '*'
    return temp_l,temp_r

s,b = list(map(int,input().split()))

while s != 0 and b != 0:        
    soldiers = [i for i in range(1,s+1)]    
    for i in range(b):
        soldiers_lr = []
        l,r = list(map(int,input().split()))        
        for j in range(l-1,r):
            soldiers[j] = 0        
        soldier_l,soldier_r = find_lr()                
        print(soldier_l,soldier_r)                    
    s,b = list(map(int,input().split()))
    print('-')
