#!/usr/bin/env/python3

def removeChar(s, c):
    s = list(s)
    s.remove(c)
    return ''.join(s)

def main():
    with open('day06.txt') as f:
        total1 = 0
        group1 = ''
        total2 = 0
        group2 = ''
        group2init = False
        for line in f:
            if line == '\n':
                total1 += len(group1)
                group1 = ''
                total2 += len(group2)
                group2 = ''
                group2init = False
            else:
                if group2 == '' and not group2init:
                    group2 = line
                    if '\n' in group2:
                        group2 = removeChar(group2, '\n')
                    group2init = True

                for c in group2:
                    if not c in line:
                        group2 = removeChar(group2, c)

                for c in line:
                    if c == '\n':
                        continue
                    elif not c in group1:
                        group1 = group1 + c


        total1 += len(group1)
        total2 += len(group2)
        print(total1, total2)

if __name__ == "__main__":
    main()
