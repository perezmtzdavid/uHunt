T = int(input())
count,total = 0,0

for case in range(T):
    answer = input()
    for charac in answer:
        if charac == 'O':
            count += 1
            total += count
        else:
            count = 0
    print(total)
    total,count = 0,0
