### Chain of responsibility só com funções


def handle_abc(letter: str) -> str:
    letters = ['a', 'b', 'c']
    if letter.lower() in letters:
        return f'handle_abc: tratou {letter}'
    return handle_def(letter)


def handle_def(letter: str) -> str:
    letters = ['d', 'e', 'f']
    if letter.lower() in letters:
        return f'handle_def: tratou {letter}'
    return handle_unsolved(letter)
    

def handle_unsolved(letter: str) -> str:
        return f'handle_unsolved: não conseguiu tratar {letter}'


if __name__ == '__main__':
    print(handle_abc('A'))
    print(handle_abc('b'))
    print(handle_abc('c'))
    print(handle_abc('D'))
    print(handle_abc('E'))
    print(handle_abc('f'))
    print(handle_abc('g'))