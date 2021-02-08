#!/usr/bin/env/python3
import re

def decToBinList(b, l):
    b = str(bin(b))[2:]
    b = '0' * (l - len(b)) + b
    return list(b)

def binListToDec(b):
    return int('0b' + ''.join(b), 2)

def applyMask(mask, value):
    b = decToBinList(value, 36)
    for i,m in enumerate(mask):
        if m != 'X':
            b[i] = m
    return binListToDec(b)

def applyMask2(mask, addr):
    addresses = []
    addr = decToBinList(addr, 36)
    n = len(re.findall('X', mask))

    for i in range(2**n):
        a = addr
        b = decToBinList(i, n)

        for j,m in enumerate(mask):
            if m == '1':
                a[j] = '1'
            elif m == 'X':
                a[j] = b.pop(0)

        addresses.append(binListToDec(a))

    return addresses

def main():
    with open('day14.txt') as f:
        memory = ['0' * 36] * (2**16)

        prog = re.compile(r'(\d+)\] = (\d+)')

        reset = f.readlines()

        for l in reset:
            if 'mask' in l:
                mask = l[7:-1]
            else:
                mem = re.findall(prog, l)[0]
                addr = int(mem[0])
                value = int(mem[1])
                memory[addr] = applyMask(mask, value)

        print(sum([int(m) for m in memory]))

        memory = {}
        for l in reset:
            if 'mask' in l:
                mask = l[7:-1]
            else:
                mem = re.findall(prog, l)[0]
                addr = int(mem[0])
                value = int(mem[1])
                addr = applyMask2(mask, addr)
                for a in addr:
                    memory[a] = value

        print(sum([int(memory[m]) for m in memory]))


if __name__ == "__main__":
    main()
