#!/usr/bin/env/python3

def main():
    with open('day12.txt') as f:
        lines = f.readlines()

        # part 1
        x = 0
        y = 0
        d = 0
        for l in lines:
            v = int(l[1:])

            if 'E' in l:
                x += v
            elif 'W' in l:
                x -= v
            elif 'N' in l:
                y -= v
            elif 'S' in l:
                y += v
            elif 'R' in l:
                d = (d + (v / 90)) % 4
            elif 'L' in l:
                d = (d - (v / 90)) % 4
            elif 'F' in l:
                if d == 0:
                    x += v
                elif d == 1:
                    y += v
                elif d == 2:
                    x -= v
                elif d == 3:
                    y -= v

        print(abs(x) + abs(y))

        # part 2:
        x = 0
        y = 0
        wx = 10
        wy = -1
        for l in lines:
            v = int(l[1:])

            if 'E' in l:
                wx += v
            elif 'W' in l:
                wx -= v
            elif 'N' in l:
                wy -= v
            elif 'S' in l:
                wy += v
            elif 'R' in l:
                while v:
                    wx, wy = -wy, wx
                    v -= 90
            elif 'L' in l:
                while v:
                    wx, wy = wy, -wx
                    v -= 90
            elif 'F' in l:
                x += (v * wx)
                y += (v * wy)

        print(abs(x) + abs(y))

if __name__ == "__main__":
    main()
