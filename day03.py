#!/usr/bin/env/python3
from functools import reduce

def getTrees(slope, stepX, stepY):
    x = 0
    y = 0
    trees = 0
    for i in range(0, len(slope), stepY):
        line = slope[i]
        if line[x] == '#':
            trees += 1
        # -1 for the \n character
        x = (x + stepX) % (len(line) - 1)
        y += 1

    return trees

def main():
    with open('day03.txt') as f:
        slope = f.readlines()

        trees = []
        for i in [1, 3, 5, 7]:
            trees.append(getTrees(slope, i, 1))

        trees.append(getTrees(slope, 1, 2))

        print(trees[1], reduce(lambda a,b:a*b, trees))

if __name__ == "__main__":
    main()
