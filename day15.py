#!/usr/bin/env/python3

def main():
    puzzle = [11, 0, 1, 10, 5, 19]

    numbers = {}
    for i,p in enumerate(puzzle):
        numbers[p] = [i]

    for i in range(6, 30000000):
        el = puzzle[-1]

        if len(numbers[el]) == 1:
            puzzle.append(0)
            numbers[0].append(i)
        else:
            diff = numbers[el][-1] - numbers[el][-2]
            puzzle.append(diff)

            if diff in numbers:
                numbers[diff].append(i)
            else:
                numbers[diff] = [i]

    print(puzzle[2019], puzzle[-1])

if __name__ == "__main__":
    main()
