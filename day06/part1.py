

def distinct_letters(segment):
    letters = {}
    for letter in segment:
        if letter in letters.keys():
            return False
        letters[letter] = 0
    return True


if __name__ == '__main__':
    with open('signal.txt') as f:
        signal = f.read().splitlines()[0]
        for i in range(len(signal)):
            if distinct_letters(signal[i:i+4]):
                print(i + 4)
                break
