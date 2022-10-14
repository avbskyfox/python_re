s = 'qweqw ewq sad arq arq das rrq3 awae awae q rqawf wefq fwf ae fwwwf'


def main():
    words = s.split(r' ')
    for i, word in enumerate(words):
        if i < len(words) - 1 and words[i] == words[i+1]:
            words.pop(i)
    print(words)


if __name__ == '__main__':
    main()
