f = open("input", "r")
lines = f.read().strip().split("\n")

# Child Bag to Parent Bag (Part A)
reverse_mapping = {}
# Parent Bag to Children Bags (Part B)
forward_mapping = {}


for line in lines:
    line = line.replace("bags", "").replace("bag", "").strip()
    parent, children = line.split("  contain ")
    children = children[:-2].split(" , ")
    for c in children:
        if c == "no other":
            pass
        else:
            num, adj, color = c.split(" ")
            num = int(num)
            child_bag = adj + " " + color

            if child_bag in reverse_mapping:
                reverse_mapping[child_bag].append(parent)
            else:
                reverse_mapping[child_bag] = [parent]
            
            if parent not in forward_mapping:
                forward_mapping[parent] = {}
            if child_bag not in forward_mapping[parent]:
                forward_mapping[parent][child_bag] = num

# Part A
def count_bags_containing(bag, containing=[]):
    if bag not in reverse_mapping:
        return containing
    
    for parent in reverse_mapping[bag]:
        if parent not in containing:
            containing.append(parent)
            containing = count_bags_containing(parent, containing)
    
    return containing

print(len(count_bags_containing('shiny gold')))

# Part B
def count_bags_inside(bag, parent_count=1):
    if bag not in forward_mapping:
        return 0
    
    result = 0
    for child in forward_mapping[bag]:
        child_count = forward_mapping[bag][child]
        result += parent_count * child_count + parent_count * count_bags_inside(child, child_count)

    return result

print(count_bags_inside('shiny gold'))
