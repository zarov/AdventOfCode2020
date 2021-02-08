#!/usr/bin/env/python3

def isValid1(minN, maxN, letter, pwd):
    count = 0
    for c in pwd:
        if c == letter:
            count += 1

    return minN <= count <= maxN

def isValid2(pos1, pos2, letter, pwd):
    return (pwd[pos1 - 1] == letter and pwd[pos2 - 1] != letter) \
        or (pwd[pos1 - 1] != letter and pwd[pos2 - 1] == letter)


def main():
    with open('day02.txt') as f:

        # part 1
        n1 = 0
        # part 2
        n2 = 0
        for line in f:
            pwd = line.split(' ')
            minMax = pwd[0].split('-')

            if isValid1(int(minMax[0]), int(minMax[1]), pwd[1][0], pwd[2]):
                n1 += 1

            if isValid2(int(minMax[0]), int(minMax[1]), pwd[1][0], pwd[2]):
                n2 += 1

        print(n1, n2)

if __name__ == "__main__":
    main()
