#!/usr/bin/env/python3

def checkSeat2(position, direction, dimension, plan):
    i = position[0]
    j = position[1]
    while 1:
        i += direction[0]
        j += direction[1]

        if -1 < i < dimension[0] and -1 < j < dimension[1]:
            if plan[i][j] == '#':
                return 1
            elif plan[i][j] == 'L':
                return 0
        else:
            return 0

def checkWhole2(plan, i, j, w, h):
    count = checkSeat2((i, j), (-1, -1), (h, w), plan)
    count += checkSeat2((i, j), (-1, 0), (h, w), plan)
    count += checkSeat2((i, j), (-1, 1), (h, w), plan)

    count = checkSeat2((i, j), (1, -1), (h, w), plan)
    count += checkSeat2((i, j), (1, 0), (h, w), plan)
    count += checkSeat2((i, j), (1, 1), (h, w), plan)

    count += checkSeat2((i, j), (0, -1), (h, w), plan)
    count += checkSeat2((i, j), (0, 1), (h, w), plan)

    return count

def checkSeat(plan, i, j, w, h):
    count = 0
    if i > 0:
        if j > 0:
            count += (plan[i - 1][j - 1] == '#') and 1 or 0
        count += (plan[i - 1][j    ] == '#') and 1 or 0
        if j < w - 1:
            count += (plan[i - 1][j + 1] == '#') and 1 or 0
    if j > 0:
        count += (plan[i    ][j - 1] == '#') and 1 or 0
    if j < w - 1:
        count += (plan[i    ][j + 1] == '#') and 1 or 0
    if i < h - 1:
        if j > 0:
            count += (plan[i + 1][j - 1] == '#') and 1 or 0
        count += (plan[i + 1][j    ] == '#') and 1 or 0
        if j < w - 1:
            count += (plan[i + 1][j + 1] == '#') and 1 or 0

    return count

def main():
    with open('day11.txt') as f:
        plan = [l[:-1] for l in f]
        plan2 = plan

        w = len(plan[0])
        w1 = w - 1
        h = len(plan)
        h1 = h - 1
        changed = True
        while changed:
            changed = False
            new = []

            for i in range(h):
                new.append([])
                for j in range(w):
                    value = plan[i][j]

                    if value == 'L':
                        count = checkSeat(plan, i, j, w, h)
                        if count == 0:
                            value = '#'
                            changed = True
                    elif value == '#':
                        count = checkSeat(plan, i, j, w, h)

                        if count >= 4:
                            value = 'L'
                            changed = True

                    new[i].append(value)

            plan = new

        # Occupied seats
        print(sum([l.count('#') for l in plan]))

        changed = True
        plan = plan2
        while changed:
            changed = False
            new = []

            for i in range(h):
                new.append([])
                for j in range(w):
                    value = plan[i][j]

                    if value == 'L':
                        count = checkWhole2(plan, i, j, h1, w1)
                        if count == 0:
                            value = '#'
                            changed = True
                    elif value == '#':
                        count = checkWhole2(plan, i, j, h1, w1)
                        if count >= 5:
                            value = 'L'
                            changed = True

                    new[i].append(value)

            plan = new

        print(sum([l.count('#') for l in plan]))

if __name__ == "__main__":
    main()
