f = open("input", "r")
lines = [int(l) for l in f]

preamble = 25

# Part A
def find_first_invalid(window):
    i = 0
    j = window
    while(i < len(lines) - window and j < len(lines)):
        num = lines[j]
        is_valid = False
        for x in range(i, j):
            for y in range(i, j):

                if x != y and lines[x] + lines[y] == num:
                    is_valid = True 

        if not is_valid:
            return num
        
        i += 1
        j += 1

invalid_num = find_first_invalid(preamble)
print(invalid_num)



# Part B helper methods
def range_sum(i, j):
    sum = 0
    for x in range(i, j+1):
        sum += lines[x]

    return sum

def find_min_max(i, j):
    mini_list = lines[i:j+1]
    mini_list.sort()
    return mini_list[0], mini_list[-1]

# Part B
def find_weakness(num):
    i = 0
    j = 1
    while(i < j and j < len(lines)):
            sum = range_sum(i, j)
            if sum < num:
                j += 1
            elif sum > num:
                i += 1
            else:
                mini, maxi = find_min_max(i, j)
                return mini + maxi

print(find_weakness(invalid_num))