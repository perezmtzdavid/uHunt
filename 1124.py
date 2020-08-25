import sys
for i in sys.stdin:
    if len(i) > 1:
        print(i.replace("\n",''))    
