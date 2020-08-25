import sys
for i in sys.stdin:
    if len(i) > 1:
        v,t = map(int, i.split())
        print(2*v*t)
    


    

