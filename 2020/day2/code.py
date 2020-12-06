with open('input') as f:

    # Part A
    valid_passwords_A = 0
    valid_passwords_B = 0
    for line in f:
        line = line.replace("-", " ").replace(":", "")
        first, second, char, password = line.split(' ')
        first = int(first)
        second = int(second)

        # Part A
        if first <= password.count(char) <= second:
            valid_passwords_A += 1

        # Part B
        if (password[first-1] == char) ^ (password[second-1] == char):
            valid_passwords_B += 1

        
    print(valid_passwords_A)
    print(valid_passwords_B)

