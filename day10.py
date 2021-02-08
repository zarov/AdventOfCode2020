#!/usr/bin/env/python3

def main():
    with open('day10.txt') as f:
        joltages = [int(j) for j in f.readlines()]
        joltages.sort()

        device = int(joltages[-1]) + 3
        joltages.append(device)

        one = []
        two = []
        three = []

        jolt = 0
        for j in joltages:
            diff = j - jolt
            if diff == 1:
                one.append(j)
            elif diff == 2:
                two.append(j)
            elif diff == 3:
                three.append(j)
            jolt = j

        print(len(one) * len(three))

        # part 2
        joltages.insert(0, 0)
        splitted = []
        seq = []
        prev = joltages.pop(0)
        seq = [prev]
        while len(joltages) > 0:
            current = joltages.pop(0)
            if (current - prev) == 3:
                splitted.append(seq)
                seq = [current]
            else:
                seq.append(current)

            prev = current

        splitted.append(seq)

        count = []
        for s in splitted:
            l = len(s)
            if l == 3:
                count.append(2)
            elif l == 4:
                count.append(4)
            elif l == 5:
                count.append(7)

        total = 1
        for c in count:
            total *= c

        print(total)

if __name__ == "__main__":
    main()
