def format_tex_quotes(text):
    result = []
    open_quote = True
    for ch in text:
        if ch == '"':
            result.append('``' if open_quote else "''")
            open_quote = not open_quote
        else:
            result.append(ch)
    return ''.join(result)

if __name__ == '__main__':
    import sys
    print(format_tex_quotes(sys.stdin.read()), end='')
