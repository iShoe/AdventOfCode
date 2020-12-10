f = open("input", "r")
lines = f.read().strip().split("\n")

# Part A
def accumulator_before_infinite_loop():
    accumulator = 0
    i = 0
    executed = set()

    while(1):
        line = lines[i]
    
        if i in executed:
            return accumulator 
        
        executed.add(i)
        op, offset = line.split(" ")

        offset = int(offset)

        if op == "acc":
            accumulator += offset
            i += 1
        elif op == "jmp":
            i += offset
        else:
            i += 1
        
print(accumulator_before_infinite_loop())


def fix_bootcode(code):
    
    accumulator = 0
    i = 0
    executed = set()
    while(1):
        if i == len(code):
            return accumulator
        
        line = code[i]
        if i in executed:
            return False 
        
        executed.add(i)
        
        op, offset = line.split(" ")
        offset = int(offset)
   
        if op == "acc":
            accumulator += offset
            i += 1
        elif op == "jmp":
            i += offset
        else:
            i += 1
        
     



for l in range(len(lines)):
    code = list(lines)
    if code[l].startswith("jmp"):
        code[l] = code[l].replace("jmp", "nop")
    elif code[l].startswith("nop"):
        code[l] = code[l].replace("nop", "jmp")

    accumulator = fix_bootcode(code)

    if accumulator:
        print(accumulator)




