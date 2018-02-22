def readrc(filename):
    filecontent = open(filename, 'r').readlines()
    kvpairs = dict()
    for linenum, line in enumerate(filecontent, 1):
        if line.strip()[0] == '#':
            continue
        key = ''
        value = ''
        valueread = False
        singlequotemode = False
        doublequotemode = False
        for char in line[:-1]:
            if char == "'" and not doublequotemode:
                singlequotemode = not singlequotemode
                continue
            if char == '"' and not singlequotemode:
                doublequotemode = not doublequotemode
                continue
            if not (singlequotemode or doublequotemode):
                if char in (' ', '\t'):
                    raise ValueError(
                        'Unerwarteter Whitespace in Zeile ' +
                        str(linenum) +
                        '!'
                    )
                if char == '#':
                    break
                if char == '=':
                    if valueread is True:
                        raise ValueError(
                            'Zwei mal = in Zeile ' +
                            str(linenum) +
                            '!'
                        )
                    valueread = True
                    continue
            if valueread:
                value += char
            else:
                key += char
        if key == '' or value == '':
            raise ValueError(
                'Unerwarteter Syntaxfehler in Zeile ' +
                str(linenum) +
                '!'
            )
        else:
            kvpairs[key] = value
    return kvpairs
