def prev_inst(inst):        
    if inst_satck[int(inst[2])-1] == 'LEFT' or inst_satck[int(inst[2])-1] == 'RIGHT':        
        return inst_satck[int(inst[2])-1]
    else:
        new_inst =inst_satck[int(inst[2])-1].split()        
        origin_inst = prev_inst(new_inst)
    return origin_inst


T = int(input())
p = 0
inst_satck = []

for case in range(T):
    num_inst = int(input())
    for i in range(num_inst):        
        inst = input()
        inst_satck.append(inst)
        if inst == 'LEFT':
            p -= 1
        elif inst == 'RIGHT':
            p += 1
        else:
            inst = inst.split()        
            val = prev_inst(inst)
            if val == 'LEFT':
                p -= 1
            elif val == 'RIGHT':
                p += 1
    print(p)
    inst_satck = []
    p=0

    
    

