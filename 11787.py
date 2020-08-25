def up(hiero):      
    count_hiero = 1
    res = hiero_values[hiero[0]]    
    for i in range(1,len(hiero)):
        if hiero_values[hiero[i]] < hiero_values[hiero[i-1]]:            
            return "error"
        if hiero[i] == hiero[i-1]:
            count_hiero += 1            
            res += hiero_values[hiero[i]]
        else:            
            res += hiero_values[hiero[i]]
            count_hiero = 1            
        if count_hiero > 9:            
            return "error"
    return res

def down(hiero):
    count_hiero = 1
    res = hiero_values[hiero[0]]
    for i in range(1,len(hiero)):
        if hiero_values[hiero[i]] > hiero_values[hiero[i-1]]:            
            return "error"
        if hiero[i] == hiero[i-1]:
            count_hiero += 1            
            res += hiero_values[hiero[i]]
        else:            
            res += hiero_values[hiero[i]]
            count_hiero = 1            
        if count_hiero > 9:            
            return "error"
    return res

hiero_values = {
    "B": 1,
    "U": 10,
    "S": 100,
    "P": 1000,
    "F": 10000,
    "T": 100000,
    "M": 1000000
}

res = 0
T = int(input())
count_hiero = 1

for test in range(T):
    hiero = input()

    ind = 1
    for i in range(1,len(hiero)):
        if hiero[0] != hiero[i]:
            ind = i

    if len(hiero) == 1:
        print(hiero_values[hiero[0]])
    elif hiero_values[hiero[0]] <= hiero_values[hiero[i]]:        
        print(up(hiero))
    elif hiero_values[hiero[0]] >= hiero_values[hiero[i]]:        
        print(down(hiero))
        

        
