import sys 

def mine_detector(m,n,field):    
    current_row = ''
    count_mines = 0
    for row in range(m):
        up = row - 1
        down = row + 1
        for col in range(n):
            left = col - 1
            right = col + 1 
            if field[row][col] == '*':                    
                    current_row += '*'
            else:
                if up >= 0:
                    if field[up][col] == '*':                    
                        count_mines += 1
                if down < m:
                    if field[down][col] == '*':                    
                        count_mines += 1
                if left >= 0:
                    if field[row][left] == '*':                    
                        count_mines += 1
                if right < n:
                    if field[row][right] == '*':                    
                        count_mines += 1
                if up >= 0 and left >= 0:                    
                    if field[up][left] == '*':                    
                        count_mines += 1
                if up >= 0 and right < n:                    
                    if field[up][right] == '*':                    
                        count_mines += 1
                if down < m and left >= 0:
                    if field[down][left] == '*':                    
                        count_mines += 1
                if down < m and right < n:
                    if field[down][right] == '*':                    
                        count_mines += 1
                current_row += str(count_mines)            
            count_mines = 0            
        print(current_row)
        current_row = ''        


line = sys.stdin.readline().split()
m,n = list(map(int,line))
num_field = 1
while m != 0 and n !=0:
    field = []
    for i in  range(m):
        field.append(sys.stdin.readline().replace('\n',''))
    print("Field #%d:"%num_field)
    mine_detector(m,n,field)    
    line = sys.stdin.readline().split()
    m,n = list(map(int,line))
    if m != 0 and n != 0:
        print()
    num_field += 1
