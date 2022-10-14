import re


def process(s):
    words = re.split(r' ', s)
    for i in range(0, len(words))
        if i < len(words) - 1 and words[i] == words[i+1]:
            words.pop(i)
    print(words)


def main():
    for i in range(1, 6):
        with open(f'2test{i}.txt') as f:
            process(f.read())


if __name__ == '__main__':
    main()
