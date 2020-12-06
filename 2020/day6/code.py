from collections import Counter

with open('input') as f:
    groups = f.read().strip().split('\n\n')
    
    # Part A
    sum = 0
    for g in groups:
        g = g.replace("\n", "")
        c = Counter(g)
        sum += len(c)

    print(sum)

    # Part B
    answered_sum = 0
    for g in groups:
        people = g.count("\n") + 1 
        g = g.replace("\n", "")
        c = Counter(g)
        for answered in c.values():
            if answered == people:
                answered_sum += 1

    print(answered_sum)
