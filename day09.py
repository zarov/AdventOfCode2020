#!/usr/bin/env/python3

def main():
    with open('day09.txt') as f:
        numbers = []
        preamble = []
        for i in range(25):
            preamble.append(int(f.readline()))
            numbers.append(preamble[i])

        l = int(f.readline())
        while l:
            numbers.append(l)
            ok = False
            for i in range(25):
                a = preamble[i]
                for j in range(25):
                    b = preamble[j]
                    if (a != b) and (a + b) == l:
                        ok = True
                        break
                if ok:
                    break

            if not ok:
                break

            preamble.pop(0)
            preamble.append(l)

            l = int(f.readline())


        invalid = l
        print(invalid)

        contigous = []
        ok = False
        while not ok:
            total = 0
            contigous = []
            for n in numbers:
                total += n
                contigous.append(n)
                if total == invalid:
                    ok = True
                    break
                elif total > invalid:
                    break

            numbers.pop(0)

        contigous.sort()
        print(contigous[0] + contigous[-1])


if __name__ == "__main__":
    main()
