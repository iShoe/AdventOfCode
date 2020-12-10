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


result = 0
def fix_boot_code(boot_code):
    global result
    accumulator = 0
    i = 0
    while(1):
    
        if i == len(boot_code):
            result = accumulator
            return True


 
        inst = boot_code[i]
        if inst['executed']:
            return False
        
        
        print(inst)

        inst['executed'] = True
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

for code_line in boot_code:
    init_op = code_line["operation"]
    if init_op in ["jmp", "nop"]:
        if init_op == "jmp":
            code_line["operation"] = "nop"
        if init_op == "nop":
            code_line["operation"] = "jmp"

        if fix_boot_code(boot_code):
            break
        else:
            code_line["operation"] = init_op
            for x in boot_code:
                x['executed'] = False


print("Part B:", result)

    
