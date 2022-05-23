def get_circle(sumators):
    d = {format(a, '03b'): '' for a in range(8)}
    for i in d:
        for j in sumators:
            d[i] += str(int(i[int(j[0]) - 1]) ^ int(i[int(j[1]) - 1]))
    return d


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


def coding(txt, sumators):
    txt2b = text_to_bits(txt)
    d = get_circle(sumators)

    shift_code = ''
    temp1 = '000'
    for i in txt2b:
        temp = i + temp1
        shift_code += d[temp[:3:]]
        temp1 = temp[:2:]

    return shift_code


def encoding(shift_code, sumators):
    d = get_circle(sumators)
    encode = ''
    temp = '000'
    for i in range(0, len(shift_code), len(sumators)):
        if int(d[('1' + temp)[:3]]) ^ int(shift_code[i:i + len(sumators)]) == 0:
            encode += '1'
            temp = ('1' + temp)[:3]
        else:
            encode += '0'
            temp = ('0' + temp)[:3]

    encode = text_from_bits(encode)
    return encode