import sys

line = sys.stdin.readline()
cheaper = []

while line:
    n,b,h,w = list(map(int,line.split()))    
    for i in range(h):        
        p = int(sys.stdin.readline())        
        a = list(map(int,sys.stdin.readline().split()))           
        for i in a:            
            if i < n:                                
                break      
        if n*p <= b:
            cheaper.append(n*p)
    cheaper.sort()
    print(cheaper[0] if cheaper else "stay home")
    cheaper = []                
    line = sys.stdin.readline()
        