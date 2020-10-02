import sys

T = int(sys.stdin.readline())
moves = 0

for case in range(T):
    s = list(sys.stdin.readline().replace('\n',''))
    t = list(sys.stdin.readline().replace('\n',''))
    zeros_s = 0
    ones_s = 0
    zeros_t = 0
    ones_t = 0
    for i in range(len(t)):
        if s[i] == '0':
            zeros_s += 1
        if s[i] == '1':
            ones_s += 1
        if t[i] == '0':
            zeros_t += 1
        if t[i] == '1':
            ones_t += 1  
    if ones_s < ones_t or zeros_s > zeros_t:     
        for i in range(len(t)):    
            if s[i] != t[i] and s[i] == '0' and zeros_s > zeros_t:
                s[i] = '1'
                ones_s += 1
                zeros_s -= 1
                moves += 1                    
    for i in range(len(t)):
        if s[i] == '?':
            if t[i] == '0':
                if zeros_s < zeros_t:
                    s[i] = '0'
                    zeros_s += 1
                    moves += 1
            elif t[i] == '1':
                if ones_s < ones_t:
                    s[i] = '1'
                    ones_s += 1
                    moves += 1
    for i in range(len(t)):
        if s[i] == '?':
            if zeros_s < zeros_t:            
                s[i] = '0'
                zeros_s += 1
                moves += 1
            if ones_s < ones_t:            
                s[i] = '1'
                ones_s += 1
                moves += 1    
    for i in range(len(t)):
        if s[i] != t[i]:
            for j in range(i+1,len(t)):
                if s[j] !=  t[j] and s[j] != s[i]:
                    temp = s[j]
                    s[j] = s[i]
                    s[i] = temp
                    moves += 1            
                    break         
    print("Case %d: %d"%(case+1,moves) if s == t else "Case %d: %d"%(case+1,-1))
    moves = 0
        


