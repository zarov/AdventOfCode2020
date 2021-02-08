#!/usr/bin/env/python3
import math

def main():
    with open('day13.txt') as f:
        timestamp = int(f.readline())
        reset = f.readline().split(',')
        buses = [int(b) for b in reset if b != 'x']
        buses = [(b * math.ceil(timestamp / b), b) for b in buses]
        buses.sort()
        print(buses[0][1] * (buses[0][0] - timestamp))

        buses = []
        for i,b in enumerate(reset):
            if b != 'x':
                buses.append((int(b), i, int(b) + i))

        #  buses.sort()
        bus = buses[0]
        step = bus[0]
        ts = 0
        index = 0
        l = len(buses)
        print(buses)
        while index < l:
            ts += step

            if (ts % bus[0]) == 0:
                ts -= bus[1]
                step = ts

                index += 1
                while index < l:
                    bus = buses[index]

                    if ((ts + bus[1]) % bus[0]) != 0:
                        break

                    index += 1

                ts += bus[1]

        print(ts)

if __name__ == "__main__":
    main()
