with open('input') as f:
	lines = [line.strip() for line in f]

height = len(lines)
width = len(lines[0])

def count_trees(right_step, down_step):	
	i = 0
	j = 0
	count = 0
	while i < height:
		if lines[i][j] == '#':
			count = count + 1
		
		j = (j + right_step) % width
		i = i + down_step
	
	return count


# Part One
result = count_trees(3,1)
print(result)

# Part Two
slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
result = 1
for s in slopes:
	result *= count_trees(s[0], s[1])
print(result)
