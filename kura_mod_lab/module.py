def without_mod(a):
    temp = ""
    d = []  # Массив для хранения числоовых значений
    p = []  # Массив для храненя знаков операций

    # Запаолнение массивов p и d знаками и числами соотвественно
    for i in a:
        if i.isdigit():
            temp += i
        else:
            d.append(int(temp))
            p.append(i)
            temp = ''
    d.append(int(temp))

    # Основной алгоритм для подсчета выражения
    while len(p):
        # Проверка, если было введено одно число
        if len(d) == 1:
            return int(d[0])
        if "*" in p:
            d[p.index('*')] *= d[p.index('*') + 1]
            d.pop(p.index('*') + 1)
            p.pop(p.index('*'))
        elif '+' in p or '-' in p:
            if not ('-' in p):
                d[p.index('+')] += d[p.index('+') + 1]
                d.pop(p.index('+') + 1)
                p.pop(p.index('+'))
            elif not ('+' in p):
                d[p.index('-')] -= d[p.index('-') + 1]
                d.pop(p.index('-') + 1)
                p.pop(p.index('-'))
            elif p.index('+') < p.index('-'):
                d[p.index('+')] += d[p.index('+') + 1]
                d.pop(p.index('+') + 1)
                p.pop(p.index('+'))
            else:
                d[p.index('-')] -= d[p.index('-') + 1]
                d.pop(p.index('-') + 1)
                p.pop(p.index('-'))

    return str(d[0])


def with_mod(a, mod):
    temp = ""
    d = []  # Массив для хранения числоовых значений
    p = []  # Массив для храненя знаков операций
    a_new = ''

    # Запаолнение массивов p и d знаками и числами соотвественно
    for i in a:
        if i.isdigit():
            temp += i
        else:
            d.append(int(temp))
            p.append(i)
            temp = ''
    d.append(int(temp))

    while '/' in p:
        d[p.index('/') + 1] = max(gcd(d[p.index('/') + 1], mod)[1:3])
        p[p.index('/')] = '*'

    for i in range(len(d)-1):
        a_new+=str(d[i])
        a_new+=p[i]
    a_new += str(d[-1])
    return a_new

def gcd(num1, num2):
    if num1 == 0:
        return [num2, 0, 1]
    else:
        div, x, y = gcd(num2 % num1, num1)
    return [div, y - (num2 // num1) * x, x]