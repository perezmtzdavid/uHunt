import sys

def one_digit(num):    
    num_str = str(num)
    val = 0
    while len(num_str) > 1:
        for i in num_str:            
            val += int(i)        
        num_str = str(val)
        val = 0
    return int(num_str)

def sum_letter(word):
    word = word.lower()
    sum_let = 0
    for i in word:
        if i.isalpha():
            sum_let += ord(i) - 96                  
    return one_digit(sum_let)

line = sys.stdin.readline()
name_one = 0
name_two = 0

while line:
    name_one = sum_letter(line)
    line = sys.stdin.readline()
    name_two = sum_letter(line)
    if name_one > name_two:
        print('{:.2f}'.format(round(100*name_two/name_one,2)).zfill(2),"%")
    else:
        print('{:.2f}'.format(round(100*name_one/name_two,2)).zfill(2),"%")
    line = sys.stdin.readline()


