T = int(input())
accepted_bag = 0
for case in range(T):
    lenght,width,depth,weight = list(map(float,input().split()))    
    eval_size = lenght + width + depth
    if lenght <= 56.0 and width <= 45.0 and depth <=25.0  and weight <= 7.0:
        print("1")
        accepted_bag += 1
    elif eval_size <= 125 and weight <= 7.0:
        print("1")
        accepted_bag += 1
    else:
        print("0")
print(accepted_bag)
