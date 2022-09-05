def main():
    RIGHT_EDGE = [*' |||']
    KEYBOARD = [
        ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'BS   '],
        ['TAB  ', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
        ['CAPS  ', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", 'ENTER'],
        ['SHIFT   ', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'SHIFT   ']
    ]
    for row in KEYBOARD:
        images = [make_key(key) for key in row] + [RIGHT_EDGE]
        show_side_by_side(images)


def show_side_by_side(images):
    for rows in zip(*images):
        for row in rows:
            print(*row, sep='', end='')
        print()


def make_key(label):
    rows = '''
@_
||
||
|/
    '''.strip().replace('@', ' ').splitlines()
    rows = [list(row) for row in rows]
    a, b, c, d = rows
    for ch in label + ' ':
        a.append('_')
        b.append(ch)
        c.append('_')
        d.append('_')
    a.append('_')
    b.append('|')
    c.append('|')
    d.append('\\')
    return rows


if __name__ == '__main__':
    main()
