import sys

lines = sys.stdin.readlines()
res = 0
count = 1

for line in lines:
    line = line.replace('\n','')
    if line != '0':        
        values = list(map(int,line.split()))
        if len(values) > 1:                
            for i in values:            
                if i > 0 and i < 100:                
                    res += 1
                else:
                    res -= 1
            print("Case %d: %d"%(count,res))
            count += 1
            res = 0 