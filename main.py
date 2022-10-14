import re


def process(s):
    words = re.split(r'\s', s)
    for i in range(0, len(words)):
        if i < len(words) - 1:
            patern = f'^{words[i]}[.,?]*$'
            if re.match(patern, words[i+1]):
                words.pop(i)
    print(words)


def main():
    for i in range(1, 2):
        with open(f'2test{i}.txt') as f:
            process(f.read())


if __name__ == '__main__':
    main()
