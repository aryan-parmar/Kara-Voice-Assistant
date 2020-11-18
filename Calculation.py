def tokened(inp):
    inp = inp.lower()
    inpToken = inp.split()
    return inpToken


def operatorChange(inp):
    index = 0
    toke = tokened(inp)
    for i in toke:
        if i == "plus":
            toke[index] = '+'
            index += 1
        elif i == "power":
            toke[index] = '**'
            index += 1
        elif i == "multiply":
            toke[index] = '*'
            index += 1
        elif i == "divide":
            toke[index] = '/'
            index += 1
        elif i == "divided":
            toke[index] = '/'
            index += 1
        elif i == "minus":
            toke[index] = '-'
            index += 1
        elif i == "into":
            toke[index] = '*'
            index += 1
        else:
            try:
                x = int(i)
                index += 1
                pass
            except:
                toke[index] = ''
                index += 1
    return toke


def detoken(inp):
    str1 = " "
    s = operatorChange(inp)
    return eval(str1.join(s))


def calc(inp):
    try:
        out = eval(inp)
        return out
    except:
        return detoken(inp)
