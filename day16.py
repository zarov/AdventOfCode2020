#!/usr/bin/env/python3
import re

def checkRule(rule, value):
    return rule[0][0] <= value <= rule[0][1] or rule[1][0] <= value <= rule[1][1]

def main():
    with open('day16.txt') as f:
        rules = {}
        ruleprog = re.compile(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)')

        line = f.readline()
        while line != '\n':
            rule = re.findall(ruleprog, line)[0]
            rules[rule[0]] = [(int(rule[1]), int(rule[2])), (int(rule[3]), int(rule[4])), rule[0]]
            line = f.readline()

        f.readline()

        myticket = [int(h) for h in f.readline().split(',')]
        fields = []
        for t in myticket:
            fields.append([rules[r] for r in rules if checkRule(rules[r], t)])

        f.readline()
        f.readline()

        error_rate = 0
        for line in f:
            ticket = [int(h) for h in line.split(',')]

            for i,t in enumerate(ticket):
                valid = False
                for r in rules:
                    if checkRule(rules[r], t):
                        valid |= True
                        break

                if not valid:
                    error_rate += t
                else:
                    for f in fields[i]:
                        if not checkRule(f, t):
                            fields[i].remove(f)

        print(error_rate)

        # remove fields, based on the ones that are sure
        fields = [(i, f) for i,f in enumerate(fields)]
        fields.sort(key=lambda f:len(f[1]))

        departure = 1
        for i,f in enumerate(fields):
            field = f[1][0]
            for g in fields[i + 1:]:
                if field in g[1]:
                    g[1].remove(field)

            if 'departure' in field[2]:
                departure *= myticket[f[0]]

        print(departure)

if __name__ == "__main__":
    main()
