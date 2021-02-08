#!/usr/bin/env/python3

def initPassport():
    return dict(byr='', iyr='', eyr='', hgt='', hcl='', ecl='', pid='', cid='')

def isValid(p):
    valid = True
    valid = valid and p['byr'] and (1920 <= int(p['byr']) <= 2002)
    valid = valid and p['iyr'] and (2010 <= int(p['iyr']) <= 2020)
    valid = valid and p['eyr'] and (2020 <= int(p['eyr']) <= 2030)

    hgt = p['hgt']
    if 'in' in hgt:
        valid = valid and (59 <= int(hgt[:-2]) <= 76)
    elif 'cm' in hgt:
        valid = valid and (150 <= int(hgt[:-2]) <= 193)
    else:
        valid = False

    hcl = p['hcl']
    if hcl:
        valid = valid and hcl[0] == '#' and len(hcl[1:]) == 6
    else:
        valid = False

    valid = valid and p['ecl'] and p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    valid = valid and p['pid'] and len(p['pid']) == 9

    return valid

def main():
    with open('day04.txt') as f:
        valid = 0
        passport = initPassport()
        for line in f:
            if line == '\n':
                if isValid(passport):
                    valid += 1

                passport = initPassport()
            else:
                fields = line.split(' ')
                for field in fields:
                    key, value = field.split(':')
                    value = value.split('\n')[0]
                    passport[key] = value

        # check last one
        if isValid(passport):
            valid += 1

        print(valid)

if __name__ == "__main__":
    main()
