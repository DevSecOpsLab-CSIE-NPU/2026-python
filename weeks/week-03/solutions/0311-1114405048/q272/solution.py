import sys

opening = True
for line in sys.stdin:
    out = []
    for ch in line:
        if ch == '"':
            if opening:
                out.append('``')
            else:
                out.append("''")
            opening = not opening
        else:
            out.append(ch)
    print(''.join(out), end='')
