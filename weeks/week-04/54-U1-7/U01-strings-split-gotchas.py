import re

def main() -> None:
    line = "asdf fjdk; afed, fjek,asdf, foo"
    fields = re.split(r"(;|,|\s)\s*", line)
    values = fields[::2]
    delimiters = fields[1::2] + [""]
    rebuilt = "".join(v + d for v, d in zip(values, delimiters))
    print(rebuilt)

    url = "http://www.python.org"
    choices = ["http:", "ftp:"]
    try:
        url.startswith(choices)
    except TypeError as error:
        print(f"TypeError: {error}")
    print(url.startswith(tuple(choices)))

    text = "  hello     world  "
    print(repr(text.strip()))
    print(repr(text.replace(" ", "")))
    print(repr(re.sub(r"\s+", " ", text.strip())))

    lines = ["  apple  \n", "  banana  \n"]
    for cleaned in (entry.strip() for entry in lines):
        print(cleaned)


if __name__ == "__main__":
    main()
