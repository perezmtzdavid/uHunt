import sys

n = int(sys.stdin.readline())
field =[]
count_star = 0
result = ''

for i in range(5):
    field.append(sys.stdin.readline().replace('\n',''))

for i in range(4*n-1):
    if field[0][i] == '*' and field[0][i-1] == '.' and field[0][i+1] == '.':
        result += '1'
    if field[0][i] == '*':
        count_star += 1
    else:
        count_star = 0    
    if count_star == 3:
        if field[3][i] == '*':
            result += '3'
        else:
            result += '2'    

print(result)
