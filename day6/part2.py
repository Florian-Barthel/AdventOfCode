
from part1 import distinct_letters


if __name__ == '__main__':
    with open('signal.txt') as f:
        signal = f.read().splitlines()[0]
        for i in range(len(signal)):
            if distinct_letters(signal[i:i+14]):
                print(i + 14)
                break
