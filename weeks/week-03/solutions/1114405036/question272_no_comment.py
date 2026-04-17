def format_tex_quotes(text):
    out = []
    open_quote = True
    for ch in text:
        if ch == '"':
            out.append('``' if open_quote else "''")
            open_quote = not open_quote
        else:
            out.append(ch)
    return ''.join(out)

if __name__ == '__main__':
    import sys
    print(format_tex_quotes(sys.stdin.read()), end='')
