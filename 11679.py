import sys

def new_line():
    return sys.stdin.readline().replace('\n','')


line = new_line()

B,N = list(map(int,line.split()))

while B != 0 and N != 0: 
    line = sys.stdin.readline()
    R = list(map(int,line.split()))
    for i in range(N):
        line = new_line()
        D,C,V = list(map(int,line.split()))
        R[D-1] -= V
        R[C-1] += V
    R.sort()
    print("S" if R[0] >= 0 else "N")
    line = new_line()
    B,N = list(map(int,line.split()))