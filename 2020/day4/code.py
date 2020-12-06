import re

def check_fields(d):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for r in required_fields:
            if r not in d:
                return False

    return True


def validate(dic):

    count = 0

    for k, v in dic.items():        
        if k == 'byr' and int(v) >= 1920 and int(v) <= 2002:
            count += 1
        if k == 'iyr' and int(v) >= 2010 and int(v) <= 2020:
            count += 1
        if k == 'eyr' and int(v) >= 2020 and int(v) <= 2030:
            count += 1
        if k == 'hgt':     
            if 'cm' in v and re.match(r'(\d{3})cm', v) and int(re.match(r'(\d{3})cm', v).groups()[0]) >= 150 and int(re.match(r'(\d{3})cm', v).groups()[0]) <= 193:
                count += 1
            elif 'in' in v and re.match(r'(\d{2})in', v) and int(re.match(r'(\d{2})in', v).groups()[0]) >= 59 and int(re.match(r'(\d{2})in', v).groups()[0]) <= 76:
                count += 1
  
        if k == 'hcl' and re.match(r'(#[0-9a-f]{6})', v):
            count += 1

        if k == 'ecl' and v in ['amb','blu','brn','gry','grn','hzl','oth']:
            count += 1
 
        if k == 'pid' and len(v) == 9 and re.match(r'(\d{9})', v):
            count += 1

    if count == 7:
        return True
    else:      
        return False
                

def is_valid_passport(d):
        if not check_fields(d):
                return False

        d = d.replace('\n', ' ').split(' ')
        dic = {}
        for i in d:
            x,y = i.split(':')
            dic[x] = y
        return validate(dic)


with open('input') as f:
    data = f.read().strip().split('\n\n')

    # Part A
    count = 0
    for d in data:
        if  check_fields(d):
            count += 1
    print('Part A', count)

    # Part B
    count = 0
    for d in data:
        if is_valid_passport(d):
            count += 1
    print('Part B', count)

