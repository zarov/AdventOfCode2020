#!/usr/bin/env/python3

def getSeat(seat, c, i):
    if c == 'L' or c == 'F':
        seat[1] -= i
    else:
        seat[0] += i


def main():
    with open('day05.txt') as f:
        seats = []
        for line in f:
            row = [0, 127]
            getSeat(row, line[0], 64)
            getSeat(row, line[1], 32)
            getSeat(row, line[2], 16)
            getSeat(row, line[3], 8)
            getSeat(row, line[4], 4)
            getSeat(row, line[5], 2)
            getSeat(row, line[6], 1)

            col = [0, 7]
            getSeat(col, line[7], 4)
            getSeat(col, line[8], 2)
            getSeat(col, line[9], 1)

            seats.append((row[0] * 8 + col[0], row[0], col[0], line[:10]))

        seats.sort(key=lambda s:s[0], reverse=True)

        # part 1
        print(seats[0][0])

        # part 2
        previous = seats[0][0]
        first_row = seats[-1][1]
        last_row = seats[0][1]

        for i in range(1, len(seats)):
            current = seats[i]
            if previous - 2 == current[0] and current[1] != first_row and current[1] != last_row:
                break
            previous = current[0]

        print(current[0] + 1)

if __name__ == "__main__":
    main()
