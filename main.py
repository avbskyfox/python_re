import re

s = 'qweqw ewq sad arq arq das rrq3 awae awae q rqawf wefq fwf ae fwwwf'


def main():
    patern = re.compile(r' ')
    words = patern.split(s)
    print(words)
    for i, word in enumerate(words):
        print(f'{i} {word}')


if __name__ == '__main__':
    main()