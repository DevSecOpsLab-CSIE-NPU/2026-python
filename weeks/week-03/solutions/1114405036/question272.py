# UVA 272: Tex Quotes
# 將每一組雙引號轉成 TeX 的 `` 和 ''

def format_tex_quotes(text):
    output = []
    open_quote = True
    for ch in text:
        if ch == '"':
            output.append('``' if open_quote else "''")
            open_quote = not open_quote
        else:
            output.append(ch)
    return ''.join(output)


def solve_272(input_text):
    return format_tex_quotes(input_text)


def main():
    import sys
    print(solve_272(sys.stdin.read()), end='')


if __name__ == '__main__':
    main()
