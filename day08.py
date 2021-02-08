#!/usr/bin/env/python3

def inverse(instruction):
    return 'nop' if instruction == 'jmp' else 'jmp'

def main():
    with open('day08.txt') as f:
        program = []
        i = 0
        for l in f:
            program.append((i, l[0:3], int(l[4:])))
            i += 1

        acc1 = 0
        done = []
        operation = program[0]
        while 1:
            if operation in done:
                break

            done.append(operation)
            index = operation[0]
            instruction = operation[1]
            value = operation[2]

            if 'acc' in instruction:
                acc1 += value
                index += 1
            elif 'jmp' in instruction:
                index += value
            else:
                index += 1

            operation = program[index]

        print(acc1)


        acc2 = 0
        done = []
        tested = []
        operation = program[0]
        testing = False
        while 1:
            if operation in done:
                operation = program[0]
                done = []
                acc2 = 0
                testing = False

            done.append(operation)
            index = operation[0]
            instruction = operation[1]
            value = operation[2]

            if not testing and (instruction == 'jmp' or instruction == 'nop') and not operation in tested:
                tested.append(operation)
                instruction = inverse(instruction)
                testing = True

            if instruction == 'acc':
                acc2 += value
                index += 1
            elif instruction == 'jmp':
                index += value
            else:
                index += 1

            if index == len(program):
                break

            operation = program[index]

        print(acc2)

if __name__ == "__main__":
    main()
