f = open("/home/aishwarya/AdventOfCode/2020/day8/input", "r")
lines = f.read().strip().split("\n")

boot_code = []
for line in lines:
    operation, offset = line.split(" ")
    sign, value = offset[:1], offset[1:]
    offset = (sign, value)
    boot_code.append({
        'operation': operation,
        'offset': offset,
        'executed': False
    })

# Part A
accumulator = 0
i = 0
while(1):
    
    inst = boot_code[i]
    if inst['executed']:
        break

    if inst['operation'] == 'acc':
        if inst['offset'][0] == '+':
            accumulator += int(inst['offset'][1])
        else:
            accumulator -= int(inst['offset'][1])
        i += 1

    elif inst['operation'] == 'jmp':
        if inst['offset'][0] == '+':
            i += int(inst['offset'][1])
        else:
            i -= int(inst['offset'][1])

    else:
        i += 1

    inst['executed'] = True

print("Part A:", accumulator)
