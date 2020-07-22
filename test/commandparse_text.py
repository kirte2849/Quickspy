def a(decoded):
    if decoded.find(' '):
        command = decoded.split(' ')[0]
        if (decoded.find('\"') == -1):
            args = decoded.split(' ')[1:]
        else:
            first = decoded.find('\"')
            last = decoded.rfind('\"')
            lstring = decoded[decoded.find(' ') + 1: first - 1]
            rstring = decoded[first + 1: last]
            if lstring.find(' ') != -1:
                args = lstring.split(' ')
                args.append(rstring)
            else:
                args = [lstring, rstring]
    else:
        command, args = decoded, []
    return command, args


b, c = a('hello 1 2 3 "sss sss sss"')
print(f'b: {b}\nc: {c}')