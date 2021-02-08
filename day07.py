#!/usr/bin/env/python3
import re

class Bag:
    def __init__(self, color):
        self.color = color
        self.visited = False
        self.children = []
        self.parents = []

    def addChild(self, child, n):
        self.children.append((int(n), child))
        child.parents.append(self)

    def __str__(self):
        n = sum([c[0] for c in self.children])
        return f"{self.color} has {len(self.parents)} parents and {n} children"

def main():
    bags = {}
    prog = re.compile(r'(\d+) (\w+ \w+)')

    with open('day07.txt') as f:
        for line in f:
            parent, children = line.split(' bags contain')

            if not parent in bags:
                bags[parent] = Bag(parent)

            children = re.findall(prog, children)

            for c in children:
                color = c[1]
                if not color in bags:
                    bags[color] = Bag(color)

                bags[parent].addChild(bags[color], c[0])

    stack = [bags['shiny gold']]
    stack[0].visited = True
    total1 = 0
    while 1:
        if len(stack) == 0:
            break

        bag = stack.pop(0)
        for p in bag.parents:
            if not p.visited:
                total1 += 1
                p.visited = True
                stack.append(p)

    print(total1)

    total2 = 0
    stack = [bags['shiny gold']]
    while 1:
        if len(stack) == 0:
            break

        bag = stack.pop(0)
        for b in bag.children:
            for i in range(b[0]):
                total2 += 1
                stack.append(b[1])

    print(total2)

if __name__ == "__main__":
    main()
