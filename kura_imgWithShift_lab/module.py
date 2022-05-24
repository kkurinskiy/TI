from random import randint

CHUNK_LENGTH = 8

assert not CHUNK_LENGTH % 8

CHECK_BITS = [i for i in range(1, CHUNK_LENGTH + 1) if not i & (i - 1)]

def randomError(r, g, b):
    r = list(bin(r)[2:].rjust(8, '0'))
    g = list(bin(g)[2:].rjust(8, '0'))
    b = list(bin(b)[2:].rjust(8, '0'))

    for i in range(2):
        t = randint(0, 7)
        if r[t] == "0":
            r[t] = '1'
        else:
            r[t] = '0'

        t = randint(0, 7)
        if g[t] == "0":
            g[t] = '1'
        else:
            g[t] = '0'

        t = randint(0, 7)
        if b[t] == "0":
            b[t] = '1'
        else:
            b[t] = '0'

    r = int(''.join(r), 2)
    g = int(''.join(g), 2)
    b = int(''.join(b), 2)

    return r, g, b