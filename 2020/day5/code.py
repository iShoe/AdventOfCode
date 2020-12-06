
def get_lines(file_path): 
    with open(file_path) as f:
        lines = f.read().strip().split('\n')
        return lines

def get_seat_id(row, column):
    return row * 8 + column

def binary_search(info, l, h):    
    for i in info:
        m = int((l+h)/2) + 1
        if i == 'F' or i == 'L':
            h = m - 1
        else:
            l = m 
        
    return l

def get_row_column(boarding_pass):
    row_info = boarding_pass[:7]
    column_info = boarding_pass[-3:]
    row = binary_search(row_info, 0, 127)    
    column = binary_search(column_info, 0, 7)
    
    return get_seat_id(row, column)
    

lines = get_lines('input')

seats = list()
for l in lines:
    
    seat_id = get_row_column(l)
    seats.append(seat_id)

seats.sort()

# Part A
maxi = seats[-1]
print(maxi)

# Part B
for x in seats[:-1]:
    if x+1 not in seats:
        print(x+1)
