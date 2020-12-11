f = open("input")
adapters = [int(l) for l in f]

adapters.sort()
adapters.insert(0,0)
adapters.append(adapters[-1] + 3)


difference = ""

for i in range(1, len(adapters)):
    diff = adapters[i] - adapters[i-1]
    difference += str(diff)

# Part A
print(difference.count("1") * difference.count("3"))

# Part B - Math way
difference = difference.split("3")
print(2**difference.count("11") * 4**difference.count("111") * 7**difference.count("1111"))

# Part B - Memoization / DP
DP = {}
def dp(i):
    if i == len(adapters) - 1: 
        return 1
    
    if i in DP:
        return DP[i]
    
    ans =  0
    for j in range(i+1, len(adapters)):
        if adapters[j] - adapters[i] <= 3:
            ans += dp(j)

    DP[i] = ans
    return ans 


print(dp(0))
    



