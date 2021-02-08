#!/usr/bin/env/python3

def main():
    with open('day01.txt') as f:
        numbers = [int(n) for n in f.readlines()]
        numbers.sort()

        # Part 1
        found = []
        for i in range(len(numbers)):
            n = numbers[i]
            for j in range(i + 1, len(numbers)):
                m = numbers[j]
                if (n + m) == 2020:
                    found = [n, m]
                    break

            if len(found) == 2:
                break

        print(found[0] * found[1])

        # Part 2
        found = []
        for i in range(len(numbers)):
            n = numbers[i]
            for j in range(i + 1, len(numbers)):
                m = numbers[j]
                for k in range(j + 1, len(numbers)):
                    o = numbers[k]
                    if (n + m + o) == 2020:
                        found = [n, m, o]
                        break

                if len(found) == 3:
                    break

            if len(found) == 3:
                break

        print(found[0] * found[1] * found[2])


if __name__ == "__main__":
    main()
