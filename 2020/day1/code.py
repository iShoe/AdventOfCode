with open('input') as f:
    data = [int(i) for i in f]

    one = [x*y for x in data for y in data if x + y == 2020][0]
    print(one)
    
    two = [x*y*z for x in data for y in data for z in data if x + y + z == 2020][0]
    print(two)
